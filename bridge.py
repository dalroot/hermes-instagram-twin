"""Bridge between Hermes Agent and TwinGraph Execution Engine."""

from __future__ import annotations

import json
import logging
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class TwinGraphBridge:
    def __init__(
        self,
        session_path: str = "",
        proxy_url: str = "",
        node_bin: str = "node",
    ) -> None:
        home_session = os.path.expanduser("~/instagram_session.json")
        if not session_path and os.path.isfile(home_session):
            session_path = home_session
        self.session_path = session_path
        self.proxy_url = proxy_url
        self.node_bin = node_bin

    def _resolve_executable(self) -> list[str]:
        """Find the twingraph CLI executable."""
        # 1. Environment variable override
        env_bin = os.environ.get("TWINGRAPH_BIN")
        if env_bin and os.path.isfile(env_bin):
            return [self.node_bin, env_bin] if env_bin.endswith(".js") else [env_bin]

        # 2. System PATH twingraph (e.g. in ~/.local/bin or global npm)
        path_bin = shutil.which("twingraph")
        if path_bin:
            return [path_bin]

        # 3. Known fallback locations
        user_local_bin = Path.home() / ".local" / "bin" / "twingraph"
        if user_local_bin.is_file():
            return [str(user_local_bin)]

        # 4. Sibling repository hopeful-bell fallback
        sibling_bin = Path(__file__).resolve().parents[1] / "hopeful-bell" / "bin" / "twingraph.js"
        if sibling_bin.is_file():
            return [self.node_bin, str(sibling_bin)]

        raise FileNotFoundError(
            "TwinGraph binary not found. Please ensure 'twingraph' is installed in PATH "
            "or set TWINGRAPH_BIN environment variable."
        )

    def execute_tool(self, tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool command through the TwinGraph runner and return parsed JSON."""
        cmd_prefix = self._resolve_executable()
        args_json = json.dumps(args, ensure_ascii=False)

        cmd = [*cmd_prefix, "call", tool_name, args_json]

        env = os.environ.copy()
        if self.proxy_url:
            env["ALL_PROXY"] = self.proxy_url
        if self.session_path:
            env["INSTAGRAM_SESSION_PATH"] = self.session_path

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                env=env,
                timeout=60,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(f"TwinGraph tool '{tool_name}' timed out after 60 seconds.") from exc
        except Exception as exc:
            raise RuntimeError(f"Failed to execute TwinGraph tool '{tool_name}': {exc}") from exc

        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()

        if result.returncode != 0:
            err_msg = stderr or stdout or f"Exited with code {result.returncode}"
            raise RuntimeError(f"TwinGraph error executing '{tool_name}': {err_msg}")

        if not stdout:
            if stderr:
                raise RuntimeError(f"TwinGraph error: {stderr}")
            return {"status": "success", "result": None}

        try:
            return json.loads(stdout)
        except json.JSONDecodeError as exc:
            lines = stdout.splitlines()
            for idx in range(len(lines) - 1, -1, -1):
                chunk = "\n".join(lines[idx:])
                try:
                    return json.loads(chunk)
                except json.JSONDecodeError:
                    continue
            raise RuntimeError(f"Failed to parse TwinGraph output as JSON: {stdout}") from exc


_bridge_instance: Optional[TwinGraphBridge] = None


def get_bridge() -> TwinGraphBridge:
    global _bridge_instance
    if _bridge_instance is None:
        _bridge_instance = TwinGraphBridge()
    return _bridge_instance


def configure_bridge(session_path: str = "", proxy_url: str = "") -> TwinGraphBridge:
    global _bridge_instance
    _bridge_instance = TwinGraphBridge(session_path=session_path, proxy_url=proxy_url)
    return _bridge_instance

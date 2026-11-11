"""Handler implementations for TwinGraph Instagram Hermes Tools."""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, Optional
from pathlib import Path

try:
    from .bridge import get_bridge
except ImportError:
    from bridge import get_bridge

logger = logging.getLogger(__name__)


def _normalize_args(args: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return dict(args or {})


def handle_get_profile(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Inspect Instagram user profile in Ghost Mode."""
    clean_args = _normalize_args(args)
    username = str(clean_args.get("username", "")).lstrip("@").strip()
    if not username:
        return json.dumps({"error": "Argument 'username' is required."}, indent=2)

    bridge = get_bridge()
    res = bridge.execute_tool("instagram_get_profile", {"username": username})
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_get_posts(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Retrieve recent posts and engagement metrics."""
    clean_args = _normalize_args(args)
    username = str(clean_args.get("username", "")).lstrip("@").strip()
    if not username:
        return json.dumps({"error": "Argument 'username' is required."}, indent=2)

    limit = int(clean_args.get("limit", 12))
    feed_type = str(clean_args.get("feed_type", "all")).strip().lower()

    bridge = get_bridge()
    res = bridge.execute_tool("instagram_get_posts", {
        "username": username,
        "limit": limit,
        "feed_type": feed_type,
    })
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_get_media_metrics(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Get metrics for a post or reel."""
    clean_args = _normalize_args(args)
    media_id = str(clean_args.get("media_id", "")).strip()
    if not media_id:
        return json.dumps({"error": "Argument 'media_id' is required."}, indent=2)

    bridge = get_bridge()
    res = bridge.execute_tool("instagram_get_media_metrics", {"media_id": media_id})
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_get_comments(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Harvest public comments on an Instagram post."""
    clean_args = _normalize_args(args)
    media_id = str(clean_args.get("media_id", "")).strip()
    if not media_id:
        return json.dumps({"error": "Argument 'media_id' is required."}, indent=2)

    limit = int(clean_args.get("limit", 25))
    bridge = get_bridge()
    res = bridge.execute_tool("instagram_get_comments", {
        "media_id": media_id,
        "limit": limit,
    })
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_search(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Search users or hashtags anonymously."""
    clean_args = _normalize_args(args)
    query = str(clean_args.get("query", "")).strip()
    if not query:
        return json.dumps({"error": "Argument 'query' is required."}, indent=2)

    search_type = str(clean_args.get("search_type", "all")).strip().lower()
    bridge = get_bridge()
    res = bridge.execute_tool("instagram_search", {
        "query": query,
        "search_type": search_type,
    })
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_audit_account(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Run an automated analytical audit on any Instagram account."""
    clean_args = _normalize_args(args)
    username = str(clean_args.get("username", "")).lstrip("@").strip()
    if not username:
        return json.dumps({"error": "Argument 'username' is required."}, indent=2)

    sample_count = int(clean_args.get("sample_count", 15))
    bridge = get_bridge()
    res = bridge.execute_tool("instagram_audit_account", {
        "username": username,
        "sample_count": sample_count,
    })
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_get_insights(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Fetch authenticated account overview or media retention curve insights."""
    clean_args = _normalize_args(args)
    metric_type = str(clean_args.get("metric_type", "overview")).strip().lower()
    period = str(clean_args.get("period", "30d")).strip()
    media_id = str(clean_args.get("media_id", "")).strip()

    bridge = get_bridge()
    res = bridge.execute_tool("instagram_get_insights", {
        "metric_type": metric_type,
        "period": period,
        "media_id": media_id,
    })
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_get_inbox(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Inspect active direct message conversations."""
    clean_args = _normalize_args(args)
    limit = int(clean_args.get("limit", 10))

    bridge = get_bridge()
    res = bridge.execute_tool("instagram_get_inbox", {"limit": limit})
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_send_message(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Send direct message to recipient (supports username or numeric PK)."""
    clean_args = _normalize_args(args)
    recipient_id = str(clean_args.get("recipient_id", "")).strip()
    text = str(clean_args.get("text", "")).strip()

    if not recipient_id or not text:
        return json.dumps({"error": "Both 'recipient_id' and 'text' are required."}, indent=2)

    bridge = get_bridge()
    res = bridge.execute_tool("instagram_send_message", {
        "recipient_id": recipient_id,
        "text": text,
    })
    return json.dumps(res, indent=2, ensure_ascii=False)


def handle_post_comment(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Post authentic comment on an Instagram post, reel, or photo."""
    clean_args = _normalize_args(args)
    media_id = str(clean_args.get("media_id", "")).strip()
    text = str(clean_args.get("text", "")).strip()

    if not media_id or not text:
        return json.dumps({"error": "Both 'media_id' and 'text' are required."}, indent=2)

    bridge = get_bridge()
    res = bridge.execute_tool("instagram_post_comment", {
        "media_id": media_id,
        "text": text,
    })
    return json.dumps(res, indent=2, ensure_ascii=False)

def handle_publish_post(args: Optional[Dict[str, Any]] = None, ctx: Any = None) -> str:
    """Request publication of a local image using an authenticated TwinGraph session.

    The engine must support `instagram_publish_post`. A failed call must never
    be reported as a successful publication; this handler performs no retries.
    """
    clean_args = _normalize_args(args)
    image_path = clean_args.get("image_path")
    caption = clean_args.get("caption", "")

    if not isinstance(image_path, str) or not image_path.strip():
        return json.dumps({"status": "error", "error": "A non-empty 'image_path' is required."})
    if not isinstance(caption, str):
        return json.dumps({"status": "error", "error": "'caption' must be a string."})

    image_file = Path(image_path).expanduser().resolve()
    if not image_file.is_file():
        return json.dumps({"status": "error", "error": "Image file not found."})

    try:
        result = get_bridge().execute_tool("instagram_publish_post", {
            "image_path": str(image_file),
            "caption": caption,
        })
    except Exception as exc:
        logger.warning("Instagram publish request failed: %s", exc)
        return json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False)

    if not isinstance(result, dict):
        return json.dumps({"status": "error", "error": "Unexpected response from publishing engine."})
    return json.dumps(result, indent=2, ensure_ascii=False)


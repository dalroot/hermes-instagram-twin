"""Handler implementations for TwinGraph Instagram Hermes Tools."""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, Optional

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

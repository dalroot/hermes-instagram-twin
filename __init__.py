"""TwinGraph Instagram Agent Plugin for Hermes Agent.

Provides deep account analytics, reel retention curves, intelligent direct messaging,
and anonymous ghost mode exploration powered by Meta Graph API v21.0 Digital Twin architecture.
"""

from __future__ import annotations

import logging
from typing import Any, List, Tuple

try:
    from .bridge import configure_bridge
    from .handlers import (
        handle_audit_account,
        handle_get_comments,
        handle_get_inbox,
        handle_get_insights,
        handle_get_media_metrics,
        handle_get_posts,
        handle_get_profile,
        handle_search,
        handle_send_message,
        handle_post_comment,
    )
    from .schemas import (
        AUDIT_ACCOUNT_SCHEMA,
        GET_COMMENTS_SCHEMA,
        GET_INBOX_SCHEMA,
        GET_INSIGHTS_SCHEMA,
        GET_MEDIA_METRICS_SCHEMA,
        GET_POSTS_SCHEMA,
        GET_PROFILE_SCHEMA,
        SEARCH_SCHEMA,
        SEND_MESSAGE_SCHEMA,
        POST_COMMENT_SCHEMA,
    )
except ImportError:
    from bridge import configure_bridge
    from handlers import (
        handle_audit_account,
        handle_get_comments,
        handle_get_inbox,
        handle_get_insights,
        handle_get_media_metrics,
        handle_get_posts,
        handle_get_profile,
        handle_search,
        handle_send_message,
        handle_post_comment,
    )
    from schemas import (
        AUDIT_ACCOUNT_SCHEMA,
        GET_COMMENTS_SCHEMA,
        GET_INBOX_SCHEMA,
        GET_INSIGHTS_SCHEMA,
        GET_MEDIA_METRICS_SCHEMA,
        GET_POSTS_SCHEMA,
        GET_PROFILE_SCHEMA,
        SEARCH_SCHEMA,
        SEND_MESSAGE_SCHEMA,
        POST_COMMENT_SCHEMA,
    )

logger = logging.getLogger(__name__)

_TOOLS: List[Tuple[str, dict, Any, str]] = [
    ("instagram_get_profile", GET_PROFILE_SCHEMA, handle_get_profile, "👤"),
    ("instagram_get_posts", GET_POSTS_SCHEMA, handle_get_posts, "📸"),
    ("instagram_get_media_metrics", GET_MEDIA_METRICS_SCHEMA, handle_get_media_metrics, "📊"),
    ("instagram_get_comments", GET_COMMENTS_SCHEMA, handle_get_comments, "💬"),
    ("instagram_search", SEARCH_SCHEMA, handle_search, "🔎"),
    ("instagram_audit_account", AUDIT_ACCOUNT_SCHEMA, handle_audit_account, "📈"),
    ("instagram_get_insights", GET_INSIGHTS_SCHEMA, handle_get_insights, "📉"),
    ("instagram_get_inbox", GET_INBOX_SCHEMA, handle_get_inbox, "📥"),
    ("instagram_send_message", SEND_MESSAGE_SCHEMA, handle_send_message, "✉️"),
    ("instagram_post_comment", POST_COMMENT_SCHEMA, handle_post_comment, "✍️"),
]


def _read_ctx_config(ctx: Any, key: str, default: Any = "") -> Any:
    if hasattr(ctx, "get_config") and callable(ctx.get_config):
        val = ctx.get_config(key, default)
        return default if val is None else val
    return default


def register(ctx: Any) -> None:
    """Standard registration entry point called by Hermes Agent plugin loader."""
    session_path = str(_read_ctx_config(ctx, "session_path", "")).strip()
    proxy_url = str(_read_ctx_config(ctx, "proxy_url", "")).strip()

    configure_bridge(session_path=session_path, proxy_url=proxy_url)

    for name, schema, handler, emoji in _TOOLS:
        try:
            ctx.register_tool(
                name=name,
                toolset="instagram",
                schema=schema,
                handler=handler,
                emoji=emoji,
            )
        except TypeError:
            ctx.register_tool(
                name=name,
                toolset="instagram",
                schema=schema,
                handler=handler,
            )

    logger.info("TwinGraph Instagram Plugin successfully registered %d tools with Hermes.", len(_TOOLS))

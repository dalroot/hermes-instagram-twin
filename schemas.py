"""OpenAI-compatible Tool Schemas for TwinGraph Instagram Hermes Plugin."""

GET_PROFILE_SCHEMA = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "description": "Instagram username / handle to inspect without @ (e.g. 'instagram' or 'cristiano')."
        }
    },
    "required": ["username"]
}

GET_POSTS_SCHEMA = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "description": "Target Instagram username."
        },
        "limit": {
            "type": "integer",
            "description": "Number of recent posts to retrieve (1-50, default 12).",
            "default": 12
        },
        "feed_type": {
            "type": "string",
            "enum": ["all", "reels", "posts"],
            "description": "Filter by content type: 'all', 'reels', or 'posts' (default: 'all').",
            "default": "all"
        }
    },
    "required": ["username"]
}

GET_MEDIA_METRICS_SCHEMA = {
    "type": "object",
    "properties": {
        "media_id": {
            "type": "string",
            "description": "Instagram media shortcode (e.g. 'Deyg1mxiobv') or full URL or numerical media ID."
        }
    },
    "required": ["media_id"]
}

GET_COMMENTS_SCHEMA = {
    "type": "object",
    "properties": {
        "media_id": {
            "type": "string",
            "description": "Instagram media shortcode or post URL."
        },
        "limit": {
            "type": "integer",
            "description": "Maximum number of public comments to harvest (default 25).",
            "default": 25
        }
    },
    "required": ["media_id"]
}

SEARCH_SCHEMA = {
    "type": "object",
    "properties": {
        "query": {
            "type": "string",
            "description": "Search keyword, username prefix, or hashtag."
        },
        "search_type": {
            "type": "string",
            "enum": ["all", "users", "hashtags"],
            "description": "Search filter type (default: 'all').",
            "default": "all"
        }
    },
    "required": ["query"]
}

AUDIT_ACCOUNT_SCHEMA = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "description": "Target Instagram username to audit."
        },
        "sample_count": {
            "type": "integer",
            "description": "Number of recent posts to sample (default 15).",
            "default": 15
        }
    },
    "required": ["username"]
}

GET_INSIGHTS_SCHEMA = {
    "type": "object",
    "properties": {
        "metric_type": {
            "type": "string",
            "enum": ["overview", "dashboard", "content", "media"],
            "description": "Type of insights: 'overview' for account metrics, 'dashboard' or 'content' for multi-dimensional content analytics & categorization, 'media' for specific media retention.",
            "default": "overview"
        },
        "media_id": {
            "type": "string",
            "description": "Required if metric_type is 'media'. The numerical ID or shortcode of the reel/post."
        },
        "period": {
            "type": "string",
            "enum": ["24h", "7d", "14d", "30d", "90d"],
            "description": "Reporting period (default: '30d').",
            "default": "30d"
        },
        "content_type": {
            "type": "string",
            "enum": ["ALL", "REEL", "POST", "STORY"],
            "description": "Filter by content type ('ALL', 'REEL', 'POST', 'STORY') when inspecting content dashboard.",
            "default": "ALL"
        },
        "category": {
            "type": "string",
            "description": "Optional category filter (e.g. 'Technology', 'Architecture', 'Announcements')."
        },
        "sort_by": {
            "type": "string",
            "enum": ["reach", "plays", "impressions", "likes", "comments", "shares", "saves"],
            "description": "Sorting metric for content dashboard (default: 'reach').",
            "default": "reach"
        }
    }
}

GET_INBOX_SCHEMA = {
    "type": "object",
    "properties": {
        "limit": {
            "type": "integer",
            "description": "Maximum number of conversation threads to inspect (default 10).",
            "default": 10
        }
    }
}

SEND_MESSAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "recipient_id": {
            "type": "string",
            "description": "Instagram username (e.g. 'cristiano') or numeric PK ID of the recipient."
        },
        "text": {
            "type": "string",
            "description": "Direct message content to send."
        }
    },
    "required": ["recipient_id", "text"]
}

POST_COMMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "media_id": {
            "type": "string",
            "description": "Instagram post URL (e.g. 'https://www.instagram.com/p/DfnMpBfADzF/'), shortcode (e.g. 'DfnMpBfADzF'), or numerical media ID."
        },
        "text": {
            "type": "string",
            "description": "Text content of the comment to post."
        }
    },
    "required": ["media_id", "text"]
}


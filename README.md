# instagram-use

> Make Instagram usable for AI agents.  
> Standardized Meta Graph API v21.0 Twin architecture, Model Context Protocol (MCP) server, and Agent plugin for autonomous Instagram workflows via session cookies or anonymous Ghost Mode.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: >=3.10](https://img.shields.io/badge/Python->=3.10-3776AB.svg)](pyproject.toml)
[![Node.js: >=18.0](https://img.shields.io/badge/Node.js->=18.0-339933.svg)](package.json)
[![Meta Graph API: v21.0](https://img.shields.io/badge/Meta%20Graph%20API-v21.0%20Twin-0081FB.svg)](https://developers.facebook.com/docs/graph-api)
[![Protocol: MCP & Hermes](https://img.shields.io/badge/Protocol-MCP%20%7C%20Hermes%20Plugin-orange.svg)](plugin.yaml)

---

## Overview

Modern AI agents need hands and eyes on social platforms, but integrating with Instagram has traditionally forced teams into one of two dead ends:
1. **The Official Meta App Wall:** Requires burdensome corporate business verification, multi-week app reviews, and severely restricted permission scopes.
2. **Fragile Web Scrapers:** Unstructured HTML parsing that breaks with every frontend release and triggers instant security checkpoints or account bans.

`instagram-use` bridges this gap. It models public actions and authenticated workflows **1:1 after the official Meta Graph API v21.0 specifications**, executing them directly through clean GraphQL and private session transports. 

Designed specifically for LLM tool-calling (Hermes, Claude Desktop/MCP, Antigravity, LangChain, CrewAI, AutoGen), `instagram-use` outputs strictly typed, structured JSON payloads with built-in safety circuit breakers.

---

## Dual Operational Modes

`instagram-use` operates in two distinct modes depending on task requirements:

```
┌────────────────────────────────────────────────────────┐
│                     instagram-use                      │
├───────────────────────────┬────────────────────────────┤
│        Ghost Mode         │     Authenticated Mode     │
│   (Zero Login / Public)   │   (Cookie Session / Auth)  │
├───────────────────────────┼────────────────────────────┤
│ • Profile Inspection      │ • Story Publishing         │
│ • Public Post / Reel Data │ • Feed Post Publishing     │
│ • Public Comment Harvest  │ • Direct Message (Send/DM) │
│ • Hashtag / User Search   │ • Direct Inbox Inspection  │
│ • Competitor Account Audit│ • Post / Reel Commenting   │
│                           │ • 30-Day Account Insights  │
└───────────────────────────┴────────────────────────────┘
```

### 1. Ghost Mode (Zero Footprint / No Login)
* **Zero Credentials Required:** No account, password, or cookies necessary.
* **Risk-Free Exploration:** Inspect competitor profiles, harvest public comment threads, scan viral reels, and search hashtags without leaving an audit trail or risking primary accounts.
* **Ideal For:** Market intelligence agents, competitor monitoring, sentiment scrapers, and trend discovery bots.

### 2. Authenticated Mode (Session-Based Digital Twin)
* **Cookie-Based Authentication:** Operates through a standard desktop session file (`instagram_session.json` containing `sessionid` and `csrftoken`). No plaintext passwords ever stored or requested.
* **Full Action Surface:** Publish stories and feed posts, respond to direct messages, post comments, and extract 30-day professional account analytics.
* **Anti-Ban Protection:** Enforces single-attempt fail-closed circuit breakers and strict string deduplication limits to protect account health.

---

## Provided Tools Reference

`instagram-use` exposes 12 deterministic tools for LLM tool calling:

| Tool | Mode | Description | Key Parameters |
| :--- | :---: | :--- | :--- |
| `instagram_publish_story` | Authenticated | Publish an ephemeral story (24-hour lifecycle). | `image_input` (path or base64) |
| `instagram_publish_post` | Authenticated | Publish a feed post with caption, hashtags, and mentions. | `image_input`, `caption` |
| `instagram_send_message` | Authenticated | Send a direct message to a user (supports handles or numeric IDs). | `recipient`, `message` |
| `instagram_get_inbox` | Authenticated | Read direct message inbox threads and unread conversations. | `limit` |
| `instagram_post_comment` | Authenticated | Post an authentic comment on any post or reel. | `media_id_or_url`, `text` |
| `instagram_get_insights` | Authenticated | Fetch 30-day professional metrics, audience curves, and reach. | `period`, `metric_type` |
| `instagram_get_profile` | Ghost | Inspect public profile details (bio, follower count, avatar). | `username` |
| `instagram_get_posts` | Ghost | Fetch recent posts/reels with like counts and engagement rates. | `username`, `count` |
| `instagram_get_media_metrics` | Ghost | Retrieve performance metrics (views, discussion count) for a reel/post. | `shortcode_or_url` |
| `instagram_get_comments` | Ghost | Harvest public comments from any post or reel without logging in. | `shortcode_or_url`, `limit` |
| `instagram_search` | Ghost | Search for users, creators, and trending hashtags anonymously. | `query` |
| `instagram_audit_account` | Ghost | Perform a comprehensive analytical audit of any public account. | `username` |

---

## Installation & Setup

### Requirements
* Python `>= 3.10`
* Node.js `>= 18.0.0`
* `twingraph` engine CLI (globally available in `PATH`)

### Option A: Install as a Hermes Agent Plugin
```bash
hermes plugins install instagram-use
```
Or clone directly into your Hermes plugins directory:
```bash
git clone https://github.com/dalroot/instagram-use.git ~/.hermes/plugins/instagram-use
```

### Option B: Use as an MCP Server (Model Context Protocol)
Add `instagram-use` to your MCP configuration (Claude Desktop, Cursor, Antigravity, etc.):

```json
{
  "mcpServers": {
    "instagram": {
      "command": "twingraph",
      "args": ["mcp"],
      "env": {
        "INSTAGRAM_SESSION_PATH": "/path/to/instagram_session.json"
      }
    }
  }
}
```

### Option C: Standalone Python / CLI Integration
Clone and install dependencies:
```bash
git clone https://github.com/dalroot/instagram-use.git
cd instagram-use
pip install -e .
```

---

## Authentication & Session Setup

For **Ghost Mode**, no authentication is required.

For **Authenticated Mode**:
1. Run the interactive session generator:
   ```bash
   twingraph login
   ```
   This opens a secure browser window for you to log in to Instagram once.
2. The session is automatically persisted to `~/instagram_session.json`.
3. Alternatively, you can supply your existing cookies manually:
   ```json
   {
     "cookies": {
       "sessionid": "YOUR_SESSION_ID",
       "ds_user_id": "YOUR_USER_ID",
       "csrftoken": "YOUR_CSRF_TOKEN"
     }
   }
   ```

---

## Safety & Circuit Breaker Architecture

Automated agents can trigger platform checkpoints if they get stuck in loops or send repetitive payloads. `instagram-use` includes built-in protective layers:

* **Single-Attempt Fail-Closed:** If an authenticated request encounters a non-200 response or security challenge, the circuit breaker immediately trips and halts execution. Automated retry loops are strictly blocked.
* **String Deduplication Caps:** Dispatches of identical comments or messages are capped at safe thresholds to prevent triggering automated spam classifiers.
* **Strict Parameter Coercion:** URLs, shortcodes, and usernames are automatically validated and resolved before executing network requests.

---

## Example Agent Prompts

```markdown
# Publishing a Story
Agent Prompt: "Publish the graphic at /tmp/announcement.jpg as an Instagram story."
Tool Called: instagram_publish_story(image_input="/tmp/announcement.jpg")

# Direct Message Inquiries
Agent Prompt: "Check our direct message inbox for any unread customer questions and summarize them."
Tool Called: instagram_get_inbox(limit=10)

# Anonymous Competitor Audit (Ghost Mode)
Agent Prompt: "Inspect the public profile @competitor_brand, calculate their average reel engagement, and summarize their top 3 recent posts."
Tools Called: 
1. instagram_get_profile(username="competitor_brand")
2. instagram_get_posts(username="competitor_brand", count=10)
```

---

## Repository Metadata & Topics

Recommended configuration for the GitHub repository:

* **Repository Name:** `instagram-use`
* **Short Description (About):**  
  *Make Instagram usable for AI agents. Meta Graph API v21.0 Twin architecture, MCP server, and Agent plugin for stories, posts, DMs, comments, and anonymous Ghost Mode.*
* **Website:** `https://github.com/dalroot/instagram-use`
* **GitHub Topics:**  
  `instagram-use`, `ai-agents`, `mcp-server`, `llm-tools`, `instagram-agent`, `agent-toolkit`, `hermes-agent`, `meta-graph-api`, `cookie-session`, `automation`

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

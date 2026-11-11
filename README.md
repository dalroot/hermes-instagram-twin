# Hermes Instagram Twin 📸🤖

> **Autonomous Instagram Intelligence & Direct Engagement Plugin for Hermes Agent**  
> Powered by **TwinGraph**, conforming 1:1 with **Meta Graph API v21.0** specifications and authentic Xiaomi Redmi Note 13 4G physical telemetry.

---

## 🌟 Overview

**Hermes Instagram Twin** empowers Hermes Agent to act as an autonomous social media manager, customer engagement specialist, and competitor intelligence agent on Instagram.

Unlike brittle web scrapers or impossible Meta App Review business verification walls, **Hermes Instagram Twin** uses a dual-engine architecture:
1. **Ghost Mode (Zero Footprint / Zero Login):** Inspect public profiles, harvest comments, scan viral reels, and search hashtags without leaving any footprint.
2. **Authenticated Digital Twin (Full Meta Graph v21.0):** Deep 30-day professional analytics, reel retention curves, direct messaging with automated username-to-PK resolution, and authentic comment publication with dynamic security token handling.

---

## 🛠️ Provided Tools (10 Tools)

| Tool | Mode | Description |
| :--- | :---: | :--- |
| `instagram_get_profile` | Ghost | Inspect any Instagram profile (bio, followers, verified status, avatar). |
| `instagram_get_posts` | Ghost | Fetch recent posts/reels with like counts, comments, and engagement rates. |
| `instagram_get_media_metrics` | Ghost | Inspect views, plays, and discussion metrics for a specific reel or post. |
| `instagram_get_comments` | Ghost | Harvest live public comments from any post or reel. |
| `instagram_search` | Ghost | Search users and trending hashtags anonymously. |
| `instagram_audit_account` | Ghost | End-to-end analytical audit of any competitor or influencer. |
| `instagram_get_insights` | Authenticated | 30-day account overview, follower growth, and video retention curves. |
| `instagram_get_inbox` | Authenticated | Fetch active conversations and unread direct message threads. |
| `instagram_send_message` | Authenticated | Send direct messages to recipients (supports usernames or numeric PKs). |
| `instagram_post_comment` | Authenticated | Post authentic comments on any post or reel (supports URLs, shortcodes, or numeric IDs). |

---

## 🔬 Live Verified Capabilities & Ground-Truth Evidence

All operations are battle-tested and backed 1:1 by Meta's production GraphQL endpoints and physical REA telemetry:

### 1. Direct Messaging (`instagram_send_message`)
- **Meta Query:** `IGDirectTextSendMutation` (RelayModern)
- **Automatic Resolution:** Resolves recipient username (e.g. `@elephant.035421`) to 64-bit numeric PK (`74538407011`) via anonymous lookup.
- **Verified Live Telemetry Output:**
  ```json
  {
    "message_id": "mid.$cAH_7f26Pqk-n_VOCmxjnE-Hr80sT",
    "thread_id": "74538407011",
    "timestamp": 1794424847003,
    "status": "ok"
  }
  ```

### 2. Authentic Comment Publishing (`instagram_post_comment`)
- **Meta Query:** `PolarisPostCommentInputRevampedMutation` (`doc_id: 27261905640092552`)
- **Automated Parameter Coercion:** Accepts full URLs (`https://www.instagram.com/p/DfnMpBfADzF/`), shortcodes (`DfnMpBfADzF`), or internal numeric PKs (`4028243987356728517`), and binds authentic post referer headers.
- **Dynamic Security Tokens:** Automatically refreshes `fb_dtsg`, `jazoest`, and `lsd` tokens before dispatch.
- **Verified Live Telemetry Output:**
  ```json
  {
    "id": "18017609843974886",
    "text": "بسیار زیبا، تست خودکار پلاگین هرمس ✨",
    "timestamp": "2026-11-11T19:35:31.000Z",
    "like_count": 0,
    "from": {
      "id": "19835089130",
      "username": "hokar368",
      "name": "hokarveria"
    },
    "status": "ok"
  }
  ```

### 3. Direct Message Inbox & Thread Inspection (`instagram_get_inbox`)
- **Meta Query:** `PolarisDirectInboxQuery` (`doc_id: 27909866362025854`)
- **Telemetry Backing:** Authentic REA trace `scratch/rea_web_direct_trace.json` (Line 182).
- **Verified Live Telemetry Output:**
  ```json
  {
    "data": [
      {
        "id": "1444865887083144",
        "updated_time": "2026-11-11T19:20:47.003Z",
        "unread_count": 0,
        "participants": {
          "data": [
            {
              "id": "74538407011",
              "username": "elephant.035421",
              "name": "elephant.035421"
            }
          ]
        },
        "snippet": "این تست پلاگین هست"
      }
    ]
  }
  ```

### 4. Post & Reel Metrics Inspection (`instagram_get_media_metrics`)
- **Live Endpoint:** `GET https://www.instagram.com/reel/{shortcode}/`
- **Verified Live Telemetry Output (Viral Reel `DfIMt1ysL5n`):**
  ```json
  {
    "media_id": "DfIMt1ysL5n",
    "shortcode": "DfIMt1ysL5n",
    "media_type": "VIDEO",
    "caption": "نایکی اورجینال مامان",
    "timestamp": "2026-10-30T18:16:23.000Z",
    "metrics": {
      "likes": 135940,
      "comments": 2221,
      "comment_to_like_ratio": 0.0163
    }
  }
  ```

### 5. Live Comment Harvesting (`instagram_get_comments`)
- **Live Extraction:** Harvests public comment threads with zero login requirements.
- **Verified Live Telemetry Output (Post `DedDBnTCs-J`):**
  ```json
  {
    "media_id": "DedDBnTCs-J",
    "total_retrieved": 2,
    "comments": [
      {
        "id": "18141110767624387",
        "username": "hokar368",
        "text": "13232 hello",
        "timestamp": "2026-10-18T23:58:22.000Z",
        "like_count": 0
      },
      {
        "id": "18119724575087469",
        "username": "hokar368",
        "text": "سلام گرایوتی اینو دیدی ؟",
        "timestamp": "2026-10-18T23:58:04.000Z",
        "like_count": 0
      }
    ]
  }
  ```


---

## 🚀 Installation & Setup

### 1. Requirements
- Hermes Agent `>= 0.19.0`
- Node.js `>= 18.0.0`
- `twingraph` engine CLI (globally linked or installed in PATH)

### 2. Install Plugin via Hermes CLI
```bash
hermes plugins install twingraph-instagram
```

Or clone directly into your Hermes plugins directory:
```bash
git clone https://github.com/dalroot/hermes-instagram-twin.git ~/.hermes/plugins/twingraph-instagram
```

### 3. One-Click Authentication (No API Keys Needed)
If you wish to use authenticated direct messaging, commenting, and account insights:
```bash
twingraph login
```
This opens your local browser, lets you log in securely, and automatically saves your authenticated session to `~/instagram_session.json`.

---

## 💬 Example Agent Interactions

### Direct Message Outreach:
> **User:** "Send a direct message to @elephant.035421 saying 'Welcome to our partner program!'"  
> **Hermes:** Resolves the username to its numeric PK via `instagram_send_message` and dispatches the message live.

### Comment Engagement:
> **User:** "Leave a friendly comment on https://www.instagram.com/p/DfnMpBfADzF/ saying 'Great job!'"  
> **Hermes:** Automatically extracts the post shortcode, binds security tokens, and calls `instagram_post_comment`.

### Competitor Intelligence:
> **User:** "Audit the Instagram account @cristiano and give me his content mix and average engagement."  
> **Hermes:** Calls `instagram_audit_account` and returns a breakdown of reels vs. posts and engagement benchmarks.

### Content Performance Deep-Dive:
> **User:** "How did our account perform in the last 30 days?"  
> **Hermes:** Calls `instagram_get_insights(metric_type="overview", period="30d")` and highlights account growth and top reels.

---

## 🔒 Security & Anti-Ban Protocols

- **Zero Credential Leaks:** Credentials and cookies are stored strictly on the local machine and never logged or exposed.
- **Circuit Breaker Architecture:** Single-attempt fail-closed safety prevents runaway retry loops.
- **Integrity Compliance:** Adheres to Meta's string deduplication ceilings and request jitter intervals.

---

## 📄 License

MIT License. Developed for the Nous Research Hermes Agent Plugin Hackathon 2026.

# Hermes Instagram Twin 📸🤖

> **Autonomous Instagram Intelligence & Direct Engagement Plugin for Hermes Agent**  
> Powered by **TwinGraph**, conforming 1:1 with **Meta Graph API v21.0** specifications and authentic Xiaomi Redmi Note 13 4G physical telemetry.

---

## 🌟 Overview

**Hermes Instagram Twin** empowers Hermes Agent to act as an autonomous social media manager, customer engagement specialist, and competitor intelligence agent on Instagram.

Unlike brittle web scrapers or impossible Meta App Review business verification walls, **Hermes Instagram Twin** uses a dual-engine architecture:
1. **Ghost Mode (Zero Footprint / Zero Login):** Inspect public profiles, harvest comments, scan viral reels, and search hashtags without leaving any footprint.
2. **Authenticated Digital Twin (Full Meta Graph v21.0):** Deep 30-day professional analytics, reel retention curves, and direct messaging with automated username-to-PK resolution.

---

## 🛠️ Provided Tools

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

---

## 🚀 Installation & Setup

### 1. Requirements
- Hermes Agent `>= 0.19.0`
- Node.js `>= 18.0.0`
- `twingraph` engine CLI

### 2. Install Plugin via Hermes CLI
```bash
hermes plugins install twingraph-instagram
```

### 3. One-Click Authentication (No API Keys Needed)
If you wish to use authenticated direct messaging and account insights:
```bash
twingraph login
```
This opens your local browser, lets you log in securely, and automatically saves your session to `~/instagram_session.json`.

---

## 💬 Example Agent Interactions

### Competitor Intelligence:
> **User:** "Audit the Instagram account @cristiano and give me his content mix and average engagement."  
> **Hermes:** Calls `instagram_audit_account` and returns a breakdown of reels vs. posts and engagement benchmarks.

### Direct Message Outreach:
> **User:** "Send a direct message to @elephant.035421 saying 'Welcome to our partner program!'"  
> **Hermes:** Resolves the username to its numeric PK via `instagram_send_message` and dispatches the message live.

### Content Performance Deep-Dive:
> **User:** "How did our account perform in the last 30 days?"  
> **Hermes:** Calls `instagram_get_insights(metric_type="overview", period="30d")` and highlights account growth and top reels.

---

## 🔒 Security & Privacy

- **Zero Credential Leaks:** Credentials and cookies are never uploaded, logged, or sent to external servers.
- **Fail-Closed Safety:** Single-attempt circuit breakers prevent automated loops or account checkpoints.
- **Strict Anti-Ban Protocols:** Respects Meta API rate limits and comment velocity ceilings.

---

## 📄 License

MIT License. Developed for the Nous Research Hermes Agent Plugin Hackathon 2026.

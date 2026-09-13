# 🛡️ AutoFix AI Engine — Enterprise Autonomous Incident Remediation

An enterprise-ready Autonomous L1 DevOps & SecOps Agent that ingests live production crashes, isolates execution environments, verifies patches via test suites, generates GitHub Pull Requests, and broadcasts team alerts—reducing MTTR from hours to under 5 seconds.

---

## 🚀 Overview

**AutoFix AI Engine** acts as a Zero-Trust Autonomous Reliability Engineer. When an application throws a runtime error in production, the engine intercepts the stack trace, runs test suites inside an isolated container sandbox, generates context-aware fixes using **Gemini 1.5 Flash**, verifies zero regressions via Pytest, and submits a human-in-the-loop (HITL) Draft PR to GitHub while alerting the engineering team on Slack.

---

## 🔌 External Apps & Integrations

| Integration | Role in System Architecture |
| :--- | :--- |
| **Sentry** | Ingests real-time stack traces and runtime crash alerts via incoming HTTP webhooks. |
| **Google Gemini 1.5 Flash** | Core LLM orchestrator responsible for root-cause analysis and code patch synthesis. |
| **GitHub API (PyGithub)** | Automated git branch creation (`ai-fix-bug-XXXX`), code commits, and Draft PR generation. |
| **Slack Webhooks** | Real-time incident telemetry, token cost breakdown, and developer notification alerts. |
| **Pytest Sandbox** | Isolated testing harness executing assertions before and after patch application. |

---

## 🛡️ Reliability, Evaluation & Enterprise Guardrails

To prevent hallucinated code or unsafe pushes from impacting main production branches:

* **Deterministic Verification Loop:** Generated code patches undergo a local Pytest assertion check inside an isolated execution container.
* **Human-in-the-Loop (HITL) Gate:** The agent never force-merges code to `main`. It opens a Draft Pull Request for developer inspection and one-click authorization.
* **Security & SAST Scanning:** Integrated static analysis verification step ensures zero hardcoded secrets or malicious vectors are introduced.
* **Audit & Cost Telemetry:** Full SOC2-compliant logging capturing execution timestamps, token consumption, and estimated model API cost.

---

## 🎥 2-Minute Demo Video

[![Watch the Demo](https://img.shields.io/badge/Demo_Video-Watch_Now-red?style=for-the-badge&logo=youtube)](YOUR_DEMO_VIDEO_URL_HERE)

> Click the link above to watch the 2-minute end-to-end incident remediation demo.

---

## ⚙️ Quickstart & Setup Guide

### 1. Prerequisites
* Python 3.10+
* Git installed locally

### 2. Installation
```bash
# Clone repository
git clone [https://github.com/Dhruv2020-code/Multi-app-ai-agent.git](https://github.com/Dhruv2020-code/Multi-app-ai-agent.git)
cd Multi-app-ai-agent

# Install dependencies
pip install -r requirements.txt

Create a .env file in the project root:
GOOGLE_API_KEY=your_gemini_api_key
GITHUB_TOKEN=your_github_personal_access_token
SLACK_WEBHOOK_URL=your_slack_incoming_webhook_url

Run the Dashboard:
streamlit run dashboard.py

### Push Command

Run these commands in your terminal to update your repository immediately:

```powershell
git add README.md
git commit -m "docs: update professional submission README"
git push origin main
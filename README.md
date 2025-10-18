# GenAI Incident Root Cause Analyzer

AI-powered, agentic assistant that analyzes **unstructured Splunk incident logs** to quickly identify **root causes** and **recommended fixes** using **AWS Bedrock, Lambda, API Gateway, Glue, Athena, S3, EventBridge, and CloudWatch**.

## What this does
- Paste incident description → get **RCA + ranked actions**.
- Correlates with **3 years of historical incidents** (Athena).
- Produces **Markdown reports** and optional notifications.

## Live Demo
*(to be added after deploy)*

## Tech Stack
AWS Bedrock · Lambda · API Gateway · Athena · Glue · S3 · EventBridge · CloudWatch

## Repo Structure
`infra/` IaC • `lambdas/` functions • `prompts/` LLM prompts & schemas • `sql/` Athena views • `web/` minimal UI • `tools/` dataset generator

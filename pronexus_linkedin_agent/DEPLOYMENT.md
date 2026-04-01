# Deployment Guide

## Fastest option: Streamlit Community Cloud

1. Create a GitHub repository and upload this folder.
2. Go to Streamlit Community Cloud.
3. Create a new app from your GitHub repo.
4. Set the main file path to `app.py`.
5. In app settings, add a secret:
   - `OPENAI_API_KEY = your_key_here`
6. Deploy.

## What to verify after deploy

- The app opens without requiring local install.
- The sidebar shows industry, topic, audience, positioning, tone, and constraints.
- Clicking **Generate new posts** produces:
  - a style guide
  - a trend brief
  - a batch of posts
  - lint output
- Clicking **Generate new posts** again produces fresh output.

## Suggested repo settings

- Make repo public for the take-home unless you have a reason not to.
- Add a short repo description such as:
  - `One-click LinkedIn post generation workflow for B2B SaaS using trend ingestion, style extraction, and LLM-based generation.`

## Suggested Streamlit app title

`Pronexus LinkedIn Post Agent`

## Fallback if deployment is delayed

If the hosted demo is not ready yet, still push the repo and include:
- GitHub repo URL
- architecture summary
- prompt file URL
- optional video demo

But the assignment explicitly asks for a hosted demo, so deployment should be prioritized.

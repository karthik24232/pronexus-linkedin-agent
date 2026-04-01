from __future__ import annotations

import json
import os
import random
from typing import List

import streamlit as st
from openai import OpenAI

from linkedin_corpus import SEED_POSTS
from prompts import (
    STYLE_GUIDE_SYSTEM,
    STYLE_GUIDE_USER,
    TREND_BRIEF_SYSTEM,
    TREND_BRIEF_USER,
    POST_GENERATION_SYSTEM,
    POST_GENERATION_USER,
    LINT_SYSTEM,
    LINT_USER,
)
from trend_sources import fetch_trend_items


DEFAULT_CONFIG = {
    "industry": "B2B SaaS founders and operators",
    "topic_focus": "agentic workflows for content and operations",
    "audience": "Founders, product leaders, and GTM operators at B2B SaaS companies",
    "positioning": "A startup that helps teams turn AI from isolated features into reliable end-to-end workflows",
    "tone": "Practical, sharp, credible, technical but accessible",
    "constraints": "No hype. No fake founder story. Prefer concrete workflows, tradeoffs, and useful takeaways.",
    "num_posts": 5,
}


st.set_page_config(page_title="Pronexus LinkedIn Agent", page_icon="✍️", layout="wide")
st.title("Pronexus LinkedIn Post Agent")
st.caption("One-click weekly batch generation for high-signal B2B LinkedIn posts.")

with st.sidebar:
    st.header("Demo configuration")
    industry = st.text_input("Industry", DEFAULT_CONFIG["industry"])
    topic_focus = st.text_input("Topic focus", DEFAULT_CONFIG["topic_focus"])
    audience = st.text_area("Audience", DEFAULT_CONFIG["audience"], height=90)
    positioning = st.text_area("Company positioning", DEFAULT_CONFIG["positioning"], height=90)
    tone = st.text_input("Tone", DEFAULT_CONFIG["tone"])
    constraints = st.text_area("Constraints", DEFAULT_CONFIG["constraints"], height=90)
    num_posts = st.slider("Posts per run", 3, 7, DEFAULT_CONFIG["num_posts"])

api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", None) if hasattr(st, "secrets") else None
client = OpenAI(api_key=api_key) if api_key else None


def call_model(system_prompt: str, user_prompt: str, temperature: float = 0.9) -> str:
    if not client:
        raise RuntimeError("OPENAI_API_KEY not configured")
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        reasoning={"effort": "medium"},
        text={"verbosity": "medium"},
    )
    return response.output_text


def fallback_style_guide() -> str:
    return (
        "Brand voice: sharp, operator-minded, specific, and calm.\n"
        "Hook patterns: contrarian claim, trend reframe, mini story, or numbered insight.\n"
        "Formatting rules: 1-line hook, short paragraphs, 3-4 bullets max, clean spacing.\n"
        "Credibility moves: use numbers, tool names, workflow details, and clear tradeoffs.\n"
        "CTA guidance: mostly none; occasionally soft invitation to compare notes.\n"
        "Avoid: vague AI hype, generic productivity claims, motivational filler, buzzword stacking.\n"
        "Checklist: concrete hook, one audience, one trend, one useful takeaway, tight close."
    )


def fallback_trend_brief(items: List[dict]) -> str:
    picks = items[:6]
    lines = []
    for i, item in enumerate(picks, 1):
        lines.append(
            f"{i}. {item['title']} ({item['source']})\n"
            f"Why it matters: shows where tooling and workflow attention are moving.\n"
            f"Audience resonance: strong for operators evaluating where AI produces real leverage.\n"
            f"Post angles: what changed, what is overhyped, and what actually ships value."
        )
    return "\n\n".join(lines)


def fallback_posts(trend_brief: str, items: List[dict], count: int) -> str:
    hook_templates = [
        "Most AI content misses the real bottleneck: operational handoffs.",
        "The teams getting value from AI are not using more prompts. They are removing more friction.",
        "A lot of people are calling this an AI trend. I think it is really a workflow design trend.",
        "3 signals tell you whether an AI workflow is real or just a demo.",
        "The interesting part of this week's AI news is not the model. It is the interface to work.",
    ]
    closes = [
        "That is the difference between a feature and a system.",
        "That is where B2B teams will get compounding leverage.",
        "The best content this year will come from operators who can explain this clearly.",
        "That is the bar I would use before adding anything new to a roadmap.",
    ]
    posts = []
    for idx in range(count):
        item = items[idx % len(items)]
        hook = random.choice(hook_templates)
        close = random.choice(closes)
        body = (
            f"Post {idx+1}\n"
            f"Hook type used: {'contrarian' if idx % 2 == 0 else 'trend_reframe'}\n\n"
            f"{hook}\n\n"
            f"This week, one useful signal came from {item['source']}: {item['title']}\n\n"
            f"For B2B SaaS teams, the takeaway is simple:\n"
            f"- do not evaluate AI in isolation\n"
            f"- evaluate the handoff between data, decisions, and actions\n"
            f"- measure whether the workflow reduces time, review load, or coordination overhead\n\n"
            f"In practice, that means asking:\n"
            f"1. What input enters the system?\n"
            f"2. What decision gets made?\n"
            f"3. What action happens next without another manual step?\n\n"
            f"{close}\n\n"
            f"Why this post should resonate: it turns a current trend into a practical operator lens instead of repeating surface-level AI news."
        )
        posts.append(body)
    return "\n\n---\n\n".join(posts)


def generate_all() -> dict:
    corpus_text = json.dumps(SEED_POSTS, indent=2)
    trend_items = fetch_trend_items()
    if not trend_items:
        trend_items = [{"source": "Fallback", "title": "Agent workflows continue to spread across SaaS", "summary": "", "published": "", "link": ""}]

    source_items_text = json.dumps(trend_items, indent=2)

    if client:
        try:
            style_guide = call_model(
                STYLE_GUIDE_SYSTEM,
                STYLE_GUIDE_USER.format(corpus=corpus_text),
            )
            trend_brief = call_model(
                TREND_BRIEF_SYSTEM,
                TREND_BRIEF_USER.format(
                    industry=industry,
                    topic_focus=topic_focus,
                    audience=audience,
                    positioning=positioning,
                    source_items=source_items_text,
                ),
            )
            posts = call_model(
                POST_GENERATION_SYSTEM,
                POST_GENERATION_USER.format(
                    num_posts=num_posts,
                    industry=industry,
                    topic_focus=topic_focus,
                    audience=audience,
                    tone=tone,
                    constraints=constraints,
                    style_guide=style_guide,
                    trend_brief=trend_brief,
                ),
            )
            lint = call_model(
                LINT_SYSTEM,
                LINT_USER.format(style_guide=style_guide, posts=posts),
            )
            return {
                "style_guide": style_guide,
                "trend_brief": trend_brief,
                "posts": posts,
                "lint": lint,
                "trend_items": trend_items,
                "mode": "live_openai",
            }
        except Exception as exc:
            st.warning(f"Live model generation failed; using fallback mode. Details: {exc}")

    style_guide = fallback_style_guide()
    trend_brief = fallback_trend_brief(trend_items)
    posts = fallback_posts(trend_brief, trend_items, num_posts)
    lint = "Fallback lint: Posts are structurally strong for a demo, but live-model mode provides better variation and sharper edits."
    return {
        "style_guide": style_guide,
        "trend_brief": trend_brief,
        "posts": posts,
        "lint": lint,
        "trend_items": trend_items,
        "mode": "fallback",
    }


col1, col2 = st.columns([1.3, 1])
with col1:
    st.subheader("Why this setup")
    st.write(
        "This demo hard-codes a practical B2B SaaS use case: generating weekly posts about agentic workflows for founders and operators. "
        "It learns style from an abstracted high-signal corpus, pulls current trend inputs from multiple sources, then generates and lints a fresh batch on each run."
    )
with col2:
    st.metric("Sources checked", "HN + Reddit + company/tooling feeds")
    st.metric("Output batch", f"{num_posts} posts")

if st.button("Generate new posts", type="primary", use_container_width=True):
    with st.spinner("Building style guide, trend brief, and weekly post batch..."):
        result = generate_all()
    st.session_state["result"] = result

if "result" in st.session_state:
    result = st.session_state["result"]
    st.success(f"Generation complete ({result['mode']}).")

    t1, t2, t3, t4 = st.tabs(["Style guide", "Trend brief", "Posts", "Lint"])
    with t1:
        st.text_area("Derived style guide", result["style_guide"], height=340)
    with t2:
        st.text_area("Trend brief", result["trend_brief"], height=340)
        with st.expander("Raw source items"):
            st.json(result["trend_items"])
    with t3:
        st.text_area("Generated batch", result["posts"], height=640)
    with t4:
        st.text_area("Post linting", result["lint"], height=420)
else:
    st.info("Click Generate new posts to run the workflow.")

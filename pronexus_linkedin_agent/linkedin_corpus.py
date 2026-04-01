"""Seed corpus of high-signal B2B LinkedIn post patterns.

This is intentionally a pattern corpus, not a copy corpus. Each example is
short, abstracted, and used only to derive structural signals.
"""

SEED_POSTS = [
    {
        "creator": "B2B Operator A",
        "notes": "Opens with a contrarian one-liner, follows with 3 compact observations, closes without hype.",
        "hook_type": "contrarian",
        "format": "short paragraphs",
        "cta": "none",
        "credibility_moves": ["specific numbers", "operational detail", "clear tradeoff"],
        "length_bucket": "medium",
        "abstract_text": "Most teams do not need more AI features. They need fewer broken handoffs. Then three short, concrete workflow lessons. Ends with a grounded recommendation."
    },
    {
        "creator": "B2B Founder B",
        "notes": "Starts with a mini-story from a product decision, then generalizes into a reusable framework.",
        "hook_type": "mini_story",
        "format": "story + bullets",
        "cta": "soft",
        "credibility_moves": ["specific scenario", "framework", "clear audience"],
        "length_bucket": "medium",
        "abstract_text": "Last quarter we shipped the wrong thing fast. Here is what we learned about prioritizing customer pain over roadmap excitement. Then four bullets."
    },
    {
        "creator": "Growth Lead C",
        "notes": "Uses numbered list with sharp formatting and one surprising metric.",
        "hook_type": "numbered_insight",
        "format": "numbered list",
        "cta": "soft",
        "credibility_moves": ["benchmark", "one memorable metric", "plain language"],
        "length_bucket": "short",
        "abstract_text": "3 things changed in B2B content this month. Each item is one sentence plus one takeaway."
    },
    {
        "creator": "Technical PM D",
        "notes": "Dense with specifics, but broken into readable lines. Avoids buzzwords.",
        "hook_type": "specific_claim",
        "format": "short paragraphs",
        "cta": "none",
        "credibility_moves": ["tool names", "workflow detail", "before/after"],
        "length_bucket": "long",
        "abstract_text": "We cut review time from hours to minutes by changing the handoff, not the model. Then explains the exact operational sequence."
    },
    {
        "creator": "AI Builder E",
        "notes": "Explains one trend through one lens for one audience. Focused and practical.",
        "hook_type": "trend_reframe",
        "format": "hook + 3 bullets + close",
        "cta": "none",
        "credibility_moves": ["one audience", "one use case", "concrete implications"],
        "length_bucket": "medium",
        "abstract_text": "Everyone is talking about agents. The better question is where agentic workflows actually beat simple automation for software teams. Then three grounded bullets."
    }
]

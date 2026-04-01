from __future__ import annotations

import time
from dataclasses import dataclass, asdict
from typing import List
import feedparser
import requests


@dataclass
class TrendItem:
    source: str
    title: str
    link: str
    summary: str
    published: str


def _clean(text: str, limit: int = 300) -> str:
    if not text:
        return ""
    text = " ".join(text.replace("\n", " ").split())
    return text[:limit] + ("..." if len(text) > limit else "")


def _parse_feed(url: str, source_name: str, limit: int = 5) -> List[TrendItem]:
    feed = feedparser.parse(url)
    items: List[TrendItem] = []
    for entry in feed.entries[:limit]:
        items.append(
            TrendItem(
                source=source_name,
                title=entry.get("title", "Untitled"),
                link=entry.get("link", ""),
                summary=_clean(entry.get("summary", entry.get("description", ""))),
                published=entry.get("published", entry.get("updated", "")),
            )
        )
    return items


def _fetch_hn(limit: int = 8) -> List[TrendItem]:
    top_ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=15).json()[:limit]
    items: List[TrendItem] = []
    for story_id in top_ids:
        story = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
            timeout=15,
        ).json()
        if not story:
            continue
        items.append(
            TrendItem(
                source="Hacker News",
                title=story.get("title", "Untitled"),
                link=story.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
                summary=_clean(story.get("text", "")),
                published=time.strftime("%Y-%m-%d", time.gmtime(story.get("time", 0))),
            )
        )
    return items


def fetch_trend_items() -> List[dict]:
    """Pulls a mixed-source trend bundle suitable for the app demo.

    Sources are intentionally lightweight and deployment-friendly:
    - Hacker News API
    - Reddit RSS feeds
    - company / tooling blog RSS feeds
    """
    items: List[TrendItem] = []

    sources = [
        ("https://www.reddit.com/r/artificial/.rss", "Reddit r/artificial"),
        ("https://www.reddit.com/r/MachineLearning/.rss", "Reddit r/MachineLearning"),
        ("https://openai.com/news/rss.xml", "OpenAI News"),
        ("https://www.anthropic.com/news/rss.xml", "Anthropic News"),
        ("https://www.producthunt.com/feed", "Product Hunt"),
    ]

    for url, source_name in sources:
        try:
            items.extend(_parse_feed(url, source_name, limit=4))
        except Exception:
            continue

    try:
        items.extend(_fetch_hn(limit=8))
    except Exception:
        pass

    deduped = []
    seen = set()
    for item in items:
        key = (item.source, item.title)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(asdict(item))

    return deduped[:24]

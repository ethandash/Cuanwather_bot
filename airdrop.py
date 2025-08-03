# airdrop.py - Ambil dari airdrops.io
import feedparser

def get_latest_airdrops():
    """Ambil 3 airdrop terbaru"""
    try:
        feed = feedparser.parse("https://airdrops.io/feed/")
        items = []
        for entry in feed.entries[:3]:
            items.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published[:16]
            })
        return items
    except:
        return []

# airdrop.py - Ambil airdrop aktif dari airdrops.io
import feedparser
from datetime import datetime

def get_active_airdrops():
    """Ambil 3 airdrop terbaru yang masih aktif (< 7 hari)"""
    try:
        feed = feedparser.parse("https://airdrops.io/feed/")
        active = []
        now = datetime.now()

        for entry in feed.entries:
            try:
                published = datetime(*entry.published_parsed[:6])
                age = (now - published).days
                if age > 7:  # Lewat 7 hari, skip
                    continue
                active.append({
                    "title": entry.title,
                    "link": entry.link,
                    "age": age,
                    "summary": entry.summary[:200] + "..." if len(entry.summary) > 200 else entry.summary
                })
            except:
                continue
            if len(active) >= 3:
                break
        return active
    except:
        return []

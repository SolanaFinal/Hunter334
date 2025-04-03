import requests
from bs4 import BeautifulSoup
import re

def fetch_tradingview_strategies(limit=5):
    url = "https://www.tradingview.com/scripts/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("[SCRAPER] Fehler beim Abrufen der Strategien.")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        script_blocks = soup.find_all("a", href=re.compile("/script/"), limit=limit)

        strategies = []
        for block in script_blocks:
            title = block.get_text(strip=True)
            href = block.get("href")
            if title and href:
                strategies.append({
                    "title": title,
                    "link": f"https://www.tradingview.com{href}"
                })

        print(f"[SCRAPER] {len(strategies)} Strategien gefunden.")
        return strategies

    except Exception as e:
        print(f"[SCRAPER] Fehler: {e}")
        return []
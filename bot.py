# =====================================================================
# PULSE Daily Summary Bot
# Fetches: Live weather (wttr.in) & Motivational quote (ZenQuotes)
# Runs automatically every single morning at 8:00 AM IST via GitHub Actions
# =====================================================================

import requests
from datetime import date

def get_weather(city="Thiruvananthapuram"):
    """Fetches today's weather as a clean one-line text summary."""
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return "Weather unavailable :("



def get_quote():
    """Fetches a random motivational quote from ZenQuotes."""
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        return f'"{quote}" - {author}'
    except Exception as e:
        return "Quote unavailable :("       


def build_summary():
    """Combines all external elements into a formatted layout block."""
    today = date.today().strftime("%B %d, %Y")
    weather = get_weather()
    quote = get_quote()
    
    summary = f"""
=========================================
PULSE Daily Summary
Date: {today}
=========================================

WEATHER REPORT:
{weather}

TODAY'S MOTIVATION:
{quote}

=========================================
"""
    return summary

def build_summary():
    """Combines all external elements into a formatted layout block."""
    today = date.today().strftime("%B %d, %Y")
    weather = get_weather()
    quote = get_quote()
    
    summary = f"""
=========================================
PULSE Daily Summary
Date: {today}
=========================================

WEATHER REPORT:
{weather}

TODAY'S MOTIVATION:
{quote}

=========================================
"""
    return summary


def run():
    """Coordinates execution: builds summary, logs it, and writes the artifact file."""
    summary = build_summary()
    print(summary)
    
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
        
    print("Pulse executed successfully.")

if __name__ == "__main__":
    run()
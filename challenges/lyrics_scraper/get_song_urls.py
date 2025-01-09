"""
retrieve song URLs for multiple artists from lyrics.com
"""
import httpx
import time

ARTISTS = [
    ("taylorswift", "https://www.lyrics.com/artist/Taylor-Swift/816977"),
    ("eminem", "https://www.lyrics.com/artist/Eminem/347307"),
    ("madonna", "https://www.lyrics.com/artist/Madonna/64565"),
    ("bobmarley", "https://www.lyrics.com/artist/Bob-Marley/2907"),
]

for artist, url in ARTISTS:
    page = httpx.get(url)
    print(artist, page.status_code)
    open(f"lyrics.com_{artist}.html", "w").write(page.text)
    time.sleep(60)

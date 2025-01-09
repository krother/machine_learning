"""
retrieve song lyrics for each artist
"""
import httpx
import os
import re
import time

from tqdm import tqdm

BASE_URL = "https://www.lyrics.com"

ARTISTS = [
    ("taylorswift", r"Taylor\+Swift"),
    ("eminem", r"Eminem"),
    ("madonna", r"Madonna"),
    ("bobmarley", r"Bob\+Marley"),
]

def filter_song_links(song_links):
    filtered = []
    titles = set()
    for url, title in song_links:
        title = re.sub(r"\[.+\]|^\s+|\s+$", "", title).strip().lower()
        if title in titles:
            continue
        filtered.append((url, title))
        titles.add(title)
    return filtered

redirects = open("redirects.txt").readlines()
redirects = set(s.strip() for s in redirects)
rf = open("redirects.txt", "a")

for artist, prefix in ARTISTS:
    fn = "lyrics.com_" + artist + ".html"
    artist = fn[11:-5]
    print(artist)

    # create folder
    cmd = f"mkdir -p lyr_{artist}"
    os.system(cmd)

    # get all song links
    html = open(fn).read()
    pattern = r"(/lyric/\d+/" + prefix + r'/[^\"]+)\"\>([^<]+)'
    song_links = re.findall(pattern, html, re.IGNORECASE)
    print(f"found {len(song_links)} urls")
    song_links = filter_song_links(song_links)
    print(f"after filtering {len(song_links)} urls")

    # download all
    for url, title in tqdm(song_links):
        try:
            title = re.sub(r"\W", "_", title)
            filename = f"{artist}/{title}.html"
            if os.path.exists(filename):
                print(filename, "exists")
                continue
            if url in redirects:
                print(filename, "in redirects")
                continue
            url = BASE_URL + url        
            page = httpx.get(url)
            print(url, page.status_code)
            if page.status_code == 200:
                open(filename, "w").write(page.text)
            elif page.status_code == 301:
                rf.write(url + "\n")
        except Exception as e:
            print("error")
            print(e)
        
        time.sleep(10)

rf.close()

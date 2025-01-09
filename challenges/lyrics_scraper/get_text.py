"""
Remove HTML and write song lyrics to a single JSON file
"""
import re
import os
import json

prefix = '<pre id="lyric-body-text" class="lyric-body" dir="ltr" data-lang="en">'

ARTISTS = [
    "taylorswift",
    "eminem",
    "madonna",
    "bobmarley",
]

out = []
for artist in ARTISTS:
    for fn in os.listdir(artist):
        s = open(artist + "/" + fn).read()
        i = s.find(prefix)
        if i > 0:
            s = s[i + len(prefix):]
            j = s.find("</pre")
            s = s[:j]
            s = re.sub(r"<[^>]*>", "", s)
            song = {
                "artist": artist,
                "title": fn[:-4],
                "text": s,
            }
            out.append(song)

open("lyrics.json", "w").write(json.dumps(out))

from __future__ import unicode_literals
import os


def c_mp3():
    link = input("""
Insert link
>""")
    try:
        os.system(f'cmd/k youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 {link}')
    except:
        print("invalid link")

# IMPORTANT: This DOES NOT work without "ffmpeg", "ffplay", and "ffprobe". Make sure you download these files and put
# in our scripts folder (where pip is). These three important files will be attached to this github.
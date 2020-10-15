from __future__ import unicode_literals
import youtube_dl
url = input("""
Insert the URL
>""")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# To convert the mkv file to mp4:
    # Type this into the command prompt/terminal
    # ffmpeg -i 123.mkv -vcodec copy 1.mp4
    # the 123.mkv should be replaced with the file name
    # 1.mp4 should be replaced with what ever you want the new file to be called


# IMPORTANT: This DOES NOT work without "ffmpeg", "ffplay", and "ffprobe". Make sure you download these files and put
# in our scripts folder (where pip is). These three important files will be attached to this github.

# more information on the gitgub
# test
# https://github.com/ShaneWD/Youtube_Downloader/tree/91c42b56823ec36f9c9c7a44420dc19f11ed15d2
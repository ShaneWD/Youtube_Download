from __future__ import unicode_literals
import youtube_dl
import os
link = input("""
Insert link
>""")
# (test link) link = "https://www.youtube.com/watch?v=JQbjS0_ZfJ0"
try:
    os.system(f'cmd /k youtube-dl --audio-format mp3 --audio-quality 6 -x {link}')
except:
    print("invalid link")

#ydl_opts = {
    #'format': 'bestaudio/best',
    #'postprocessors': [{
        #'key': 'FFmpegExtractAudio',
        #'preferredcodec': 'mp3',
        #'preferredquality': '320',
    #}],
#}

#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #ydl.download([link])

# credit: https://github.com/silvanohirtie/youtube-mp3-downloader

# IMPORTANT: This DOES NOT work without "ffmpeg", "ffplay", and "ffprobe". Make sure you download these files and put
# in our scripts folder (where pip is). These three important files will be attached to this github.
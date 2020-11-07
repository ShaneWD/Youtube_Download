from MP3 import c_mp3
from MP4 import c_mp4

request = input("""
Do you want to download music from youtube or just audio
"Video" = Download the YouTube video along with the audio (same file)
"Audio" = Download just the YouTube audio in mp3 format
Video OR Audio?
>""").lower()

if request == "mp4" or request == "video":
    c_mp4()

if request == "mp3" or request == "audio":
    c_mp3()

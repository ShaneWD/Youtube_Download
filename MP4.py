from __future__ import unicode_literals
import os


def convert():
    original_name = input("""
Mandatory: If the name of the file contains any spaces, rename it to something else that does not contain spaces
What is the file name called?
>""")
    new_name = input("""
What would you like to call the new file?
Remember, the new name CANNOT contain any spaces
(Type "!stay" if you don't want to change the name)
>""")
    if new_name.lower() == "!stay":
        new_name = original_name
    os.system(f'ffmpeg -i {original_name} -vcodec copy {new_name}')


url = input("""
Insert the URL
or 
Type "convert" to convert a file to MP4 format
>""")
if url.lower() != "convert":
    try:
        os.system(f'cmd /k youtube-dl {url}')
        video_format = input("""
    The file was downloaded as a WEBM file. 
    Would you like to have it be a MP4 file?
    Yes or No?""").lower()
        if video_format == "yes":
            convert()
        if video_format == "no":
            pass
    except:
        print("invalid link")
elif url.lower() == "convert":
    convert()

#ydl_opts = {}
#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #ydl.download([url])

# To convert the mkv file to mp4:
    # Type this into the command prompt/terminal
    # ffmpeg -i 123.mkv -vcodec copy 1.mp4
    # the 123.mkv should be replaced with the file name
    # 1.mp4 should be replaced with what ever you want the new file to be called


# IMPORTANT: This DOES NOT work without "ffmpeg", "ffplay", and "ffprobe". Make sure you download these files and put
# in our scripts folder (where pip is). These three important files will be attached to this github.

# more information on the gitgub
# test
# https://github.com/ShaneWD/Youtube_Download
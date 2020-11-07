from __future__ import unicode_literals
import os


def c_mp4():
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
            os.system(f'youtube-dl {url}')
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

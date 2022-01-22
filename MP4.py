from __future__ import unicode_literals
import os


def c_mp4():
    def convert():
        original_name = input("""What is the file name called? Make sure to include file type.
(ex: concert.WEBM)

>""").replace(" ", "?")
        new_name = input("""
What would you like to call the new file?
(Type "!stay" if you don't want to change the name)
Make sure to include file type.
(ex: concert.MP4)

>""").replace(" ", "?")
        if new_name.lower() == "!stay":
            new_name = original_name

        os.system(f"""ffmpeg -i "{original_name.replace("?", " ")}" -vcodec copy "{new_name.replace("?", " ")}" """)

    url = input("""
Insert the URL
or 
Type "convert" to convert a file to MP4 format
>""")

    if url.lower() == "convert":
        convert()

    else:
        try:
            os.system(f'youtube-dl {url}')
            video_format = input("""
The file was downloaded as a WEBM file. 
Would you like to have it be a MP4 file?
Yes or No?""").lower()
            if video_format.lower() == "yes":
                convert()
            elif video_format.lower() == "no":
                pass
            else:
                print("Invalid response. Please try again. ")

        except:
            print("Invalid link. Please try again.")
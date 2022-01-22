from __future__ import unicode_literals
import os


def c_mp4():
    def convert():
        original_name = input("""What is the file name called?
>""").replace(" ", "-")
        new_name = input("""
What would you like to call the new file?
(Type "!stay" if you don't want to change the name)

>""").replace(" ", "-")
        if new_name.lower() == "!stay":
            new_name = original_name
        os.system(f"""ffmpeg -i "{original_name.replace("-", " ")}" -vcodec copy "{new_name.replace("-", " ")}" """)

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
            if video_format.lower() == "yes":
                convert()
            elif video_format.lower() == "no":
                pass
            else:
                print("invalid response")
        except:
            print("Invalid link. Please try again.")
            
    elif url.lower() == "convert":
        convert()

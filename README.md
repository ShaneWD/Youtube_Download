# Youtube_Download

## Download Videos and Music from YouTube. For Free!
A youtube downloader. Uses the modules: "yt-dlp", "FFmpeg", "FFplay", and "FFprobe". These modules cannot be pip installed, they have to download externally.  I have included these modules on this GitHub page. Make sure these four modules are stored where modules are normally stored to be referenced by your specific project. 


## Necessities

```bash

yt-dlp

FFmpeg

FFplay

FFprobe
```


## Download Videos

```python
from __future__ import unicode_literals
import os

link = input("""What is the YouTube link?
>""")

os.system(f'yt-dlp {link}')
```

## Download Music

```python
from __future__ import unicode_literals
import os

link = input("""What is the YouTube link?
>""")

os.system(f'yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 {link}')
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Suggesting changes are fine, however, be descriptive.


## My Youtube
[Shane Dsi](https://www.youtube.com/channel/UCfRjte3cG1e9YI_cce_0oPQ)



# floh4x
Download videos off flograppling CDN

Uses python 3.

You need:
- ffmpeg installed on your computer (http://jollejolles.com/install-ffmpeg-on-mac-os-x/)
- Python 3.x installed
- pip (package manager) installed

See https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos for help on this.

First, install requirements with `pip install -Ur requirements.txt`
Usage:
```
python main.py https://www.flograppling.com/video/6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship
```

It will download the file to `6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship.mp4` in the directory you run it in.

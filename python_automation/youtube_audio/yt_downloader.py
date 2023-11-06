''' Download audio from youtube url '''
from pytube import YouTube
import sys
import os

url = input("What youtube url would you like the transcript for?")

yt = YouTube(url)
print(yt.title)
print(yt.streams.filter(only_audio=True))
stream = yt.streams.get_by_itag(140)
stream.download()


#!/usr/bin/env python3

from pytube import YouTube

def banner():
    '''Display banner'''
    print("\nDownload your favourites videos from youtube\n")

def download():
    try:
        tubeURL=input("Enter the Youtube  video URL to download: ")
        yt_obj = YouTube(tubeURL)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    
        # download the highest quality video
        filters.get_highest_resolution().download()
        print('\nVideo Downloaded Successfully\n')
    except Exception as e:
        print(e)


def main():
    banner()
    download()

if __name__ == "__main__":
    main()
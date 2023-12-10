import lmproof
import tabula
import PIL
from PIL import Image
from tkinter.filedialog import *
import pytube
from pygame import mixer
from gtts import gTTS
import os
import img2pdf
from fpdf import FPDF
from difflib import SequenceMatcher
from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys


def proofreading():
    text = input("Enter the text to proofread: ")
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))


def pdf_to_csv():
    filename = input("Enter PDF File Path: ")
    df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')
    df.to_csv('output.csv')


def images_to_pdf():
    fl = askopenfilenames()
    img = Image.open(fl[0])
    img.save("output.jpg", "JPEG", optimize=True, quality=10)


def download_youtube_video():
    link = input('Enter YouTube Video URL: ')
    video_download = pytube.YouTube(link)
    video_download.streams.first().download()
    print('Video Downloaded:', link)


def text_to_speech():
    tts = gTTS('Like This Article')
    tts.save('output.mp3')
    mixer.init()
    mixer.music.load('output.mp3')
    mixer.music.play()


def create_pdf_with_images():
    Pdf = FPDF()
    list_of_images = ["wall.jpg", "nature.jpg", "cat.jpg"]

    for i in list_of_images:
        Pdf.add_page()
        Pdf.image(i, x, y, w, h)

    Pdf.output("result.pdf", "F")


def plagiarism_checker():
    f1 = input("Enter file_1 path: ")
    f2 = input("Enter file_2 path: ")

    with open(f1, errors="ignore") as file1, open(f2, errors="ignore") as file2:
        f1_data = file1.read()
        f2_data = file2.read()
        res = SequenceMatcher(None, f1_data, f2_data).ratio()

    print(f"These files are {res*100} % similar")


def url_shortening():
    for tinyurl in map(make_tiny, sys.argv[1:]):
        print(tinyurl)


def make_tiny(url):
    request_url = ('http://tinyurl.com/app-index.php?' +
                   urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def main():
    while True:
        print("\nChoose an option:")
        print("1. Proofreading")
        print("2. PDF to CSV")
        print("3. Images to PDF")
        print("4. Download YouTube Video")
        print("5. Text to Speech")
        print("6. Create PDF with Images")
        print("7. Plagiarism Checker")
        print("8. URL Shortening")
        print("9. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            proofreading()
        elif choice == "2":
            pdf_to_csv()
        elif choice == "3":
            images_to_pdf()
        elif choice == "4":
            download_youtube_video()
        elif choice == "5":
            text_to_speech()
        elif choice == "6":
            create_pdf_with_images()
        elif choice == "7":
            plagiarism_checker()
        elif choice == "8":
            url_shortening()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()

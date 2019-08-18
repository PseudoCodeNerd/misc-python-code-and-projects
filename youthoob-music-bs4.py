'''
@author: Madhav (/PseudoCodeNerd)

I'm really liking BS4 and requests nowadays!

Enter song name and it will show you the most similar matching video.
'''
import os
import webbrowser

import requests 
from bs4 import BeautifulSoup

inp_func = None

try:
    inp_func = raw_input('Enter Song (T-Series Rules!) : ')
except NameError:
    inp_func = input('Enter Song (T-Series Rules!) : ')
    
slicee = inp_func.replace(' ','+')

# search for the best similar matching video
url = 'https://www.youtube.com/results?search_query=' + slicee
source_code = requests.get(url,timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

#fetch url of vid
songs = soup.findAll('div', {'class': 'yt-lockup-video'})
song = songs[0].contents[0].contents[0].contents[0]

try:
    link = song['href']
    webbrowser.open('https://www.youtube.com' + link)
except KeyError:
    print("Can't find any song.\nP.S: Perhaps it's from Sweden\n\tPlease search for any other T-Series Song!")
    
'''
Songs which I have tried:
1. Despacito (obviously lol!)
2. Bitch Lasagna (F)
3. Hindustani Bhau (not a song, but still...)
4. Mandir Vahin Banayenge _/\_
'''
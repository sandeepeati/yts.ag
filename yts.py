from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import urllib.parse
from html.parser import HTMLParser

print('\n')
movieName = input("MOVIE NAME: ")
baseurl = 'https://www.yts.ag/browse-movies?page='
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

# searches movie in the page

def movieSearch(name):
    for i in links:
        if i.string != None:
            j = i.string.lower()
            if j == name:
                return i.get('href')
    return False

# creates a torrent file of the movie if the user chooses to

def downloadMovie(movielink):
    moviesoup = BeautifulSoup(urlopen(Request(movielink, headers=header)), 'html.parser')
    movie_links = moviesoup.find_all('a')
    for i in range(0,len(movie_links)):
        j = movie_links[i].string
        if j != None and j == '720p':
            t = urlopen(Request(movie_links[i].get('href'), headers=header)).read()
            f = open(movieName + ".torrent", 'wb')
            f.write(t)
            f.close()



MaxPages = 305
link = []

# looping through all pages of yts.ag and searching for the movie
for i in range(1,MaxPages+1):
    links = []
    url = baseurl + str(i)
    soup = BeautifulSoup(urlopen(Request(url, headers=header)), 'html.parser')
    links = soup.find_all('a')
    status = movieSearch(movieName)
    if status != False:
        download = input("Do you want to download torrent file(720p):(y/n) ")
        if download == 'y':
            downloadMovie(status)
            break
        else:
            print(status)
            break
    print('End of page ',i)


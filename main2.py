import os
import re
import requests

import graphics
from graphics import *
class GenreWindow:
    def __init__(self, height, width, type):
        self.height = height
        self.width = width
        self.type = type
    def setHeight(self, height):
        self.height = height
    def setWidth(self, width):
        self.width = width
    def setType(self, type):
        self.type = type
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def getType(self):
        return self.type
    def getWindow(self):
        return self
    def checkM(self):
        x = self.checkMouse()
        print(x)
        return x
    def drawWindow(self):
        if self.type == 0:
            #set up the screen and the background
            win = GraphWin("Genre Classifier", self.width, self.height)
            background = Rectangle(Point(0, 0), Point(self.width, self.height))
            background.setFill("#BDB76B")
            background.setOutline("#BDB76B")
            background.draw(win)
            #draw all the details.
            #draw cards for every genre
            #set initial points for the first card
            #also set the height change and width change to make it more general.
            Xinit = 0.02*self.width
            Yinit = 0.16*self.height
            Xchange = 0.16*self.width
            Ychange = 0.2*self.height
            XinitText = Xinit + 0.5*Xchange
            YinitText = Yinit + 0.5*Ychange
            #draw a table with 6 columns and 3 rows
            #Write the text in the boxes.
            #make a list of all the words to draw in the boxes.
            WordList = ["action", "comedy", "adventure","animation","documentary","horror","romance","Sci-fi","music","thriller","western","adventure","war","crime","fantasy","family","drama","mystery"]
            valueControl = 0
            for j in range(3):
                try:
                    x = valueControl
                    for i in range(x, x+6):
                        #make the texts in the boxes.
                        textWord = WordList[valueControl]
                        text = Text(Point(XinitText, YinitText), textWord)
                        card = Rectangle(Point(Xinit, Yinit), Point(Xinit + Xchange, Yinit + Ychange))
                        card.setFill("#F0E68C")
                        Xinit += Xchange
                        XinitText += Xchange
                        card.draw(win)
                        text.draw(win)
                        valueControl += 1
                except:
                    pass
                Xinit = 0.02*self.width
                XinitText = Xinit + 0.5 * Xchange
                Yinit += Ychange
                YinitText += Ychange
        return win
    #function to draw a space to put the names of all the movies on after search
    def drawBlankSheet(self, lst):
        win = GraphWin("Genre Classifier", self.width, self.height)
        background = Rectangle(Point(0, 0), Point(self.width, self.height))
        background.setFill("#BDB76B")
        background.setOutline("#BDB76B")
        background.draw(win)

        Xinit = 0.15 * self.width
        Yinit = 0.16 * self.height
        Xchange = 0.3 * self.width
        Ychange = 25
        if len(lst) < 15:
            lcv = 1
        elif len(lst) >= 15 and len(lst) < 30:
            lcv = 2
        elif len(lst) >= 30:
            lcv = 3
        x = 0
        for i in range(lcv):
            try:
                for j in range(15):
                    text = Text(Point(Xinit, Yinit), lst[x+j])
                    text.draw(win)
                    Yinit+=Ychange
                x += 15
                Xinit += Xchange
                Yinit = 0.16*self.height
            except:
                pass

def app(win, q):

    #apikey = 08d24012d752c9e551f35a3516460668
    mn = open("moviename.txt", "w")
    comedy = open("comedy.txt", "w")
    action = open("action.txt", "w")
    adventure = open("adventure.txt", "w")
    animation = open("animation.txt", "w")
    documentary = open("documentary.txt", "w")
    horror = open("horror.txt", "w")
    romance = open("romance.txt", "w")
    scifi = open("scifi.txt", "w")
    music = open("music.txt", "w")
    thriller = open("thriller.txt", "w")
    western = open("western.txt", "w")
    adventure = open("adventure.txt", "w")
    war = open("war.txt", "w")
    crime = open("crime.txt", "w")
    fantasy = open("fantasy.txt", "w")
    family = open("family.txt", "w")
    drama = open("drama.txt", "w")
    mystery = open("mystery.txt", "w")


    #
    for root, dirs, files in os.walk(r"C:\Users\Yeab\Desktop\desktop\summer movies"):
        for file in files:
            #print(file)
            if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".mkv") or file.endswith(".wav") or file.endswith(".mov") or file.endswith(".flv"):
                global stringdir

                stringdir = str(dirs)
                filepath = os.path.join(root, file)
                stringpath = str(dirs)
                statinfo = os.stat(filepath).st_size

                if statinfo > 400000000:
                    file = file.replace(".", " ")
                    sFile = file.split(" ")
                    listfile = list(sFile)
                    try:
                        j = file[0:file.index("2")]
                        #j = file[0:file.index("1")]
                    except:
                        pass
                    #get rid of anything that comes after a (.
                    for item in j:
                        if item[0] == "(":
                            j = j[0:j.index(item)]
                    #j = line.rstrip("\n")  # get rid of newline characters
                    #response = requests.get(url + movieTitle)
                    if j.endswith(" "):
                        listj = list(j)
                        del(listj[-1])
                        #j = str(listj)
                        str1 = ''.join(listj)

                    Fname = str1.replace(" ", "+")

                    url = "http://www.omdbapi.com/?s={}&apikey=8af7d872".format(Fname)
                    url2 = "http://api.themoviedb.org/3/search/movie?api_key=08d24012d752c9e551f35a3516460668&query={}".format(Fname)
                    #print(url2)
                    response = requests.get(url2)
                    jsonobj = response.json()

                    if response.status_code == 200:
                        jsonstr = str(jsonobj)
                        jsonlist = list(jsonstr)
                        #print(jsonobj)
                        search = jsonobj.get("results")
                        innermost = search[0]
                        #print(innermost)
                        if innermost.get('genre_ids') == None:
                            print("Genre Not Found!")
                        else:
                            #print(jsonobj['results'][0]['genre_ids'])
                            string_genre = str(jsonobj['results'][0]['genre_ids'])
                            x = ''.join(string_genre)
                            #print(x)

                            if '28' in string_genre and q == "action":
                                print(j)
                                action.write(j)
                                action.write("\n")
                            if '16' in string_genre and q == "animation":
                                print(j)
                                animation.write(j)
                                animation.write("\n")
                            if '99' in string_genre and q == "documentary":
                                print(j)
                                documentary.write(j)
                                documentary.write("\n")
                            if '18' in string_genre and q == "drama":
                                print(j)
                                drama.write(j)
                                drama.write("\n")
                            if '10751' in string_genre and q == "family":
                                print(j)
                                family.write(j)
                                family.write("\n")
                            if '14' in string_genre and q == "fantasy":
                                print(j)
                                fantasy.write(j)
                                fantasy.write("\n")
                            if '36' in string_genre and q == "history":
                                print(j)
                                history.write(j)
                                history.write("\n")
                            if '35' in string_genre and q == "comedy":
                                print(j)
                                comedy.write(j)
                                comedy.write("\n")
                            if '10752' in string_genre and q == "war":
                                print(j)
                                war.write(j)
                                war.write("\n")
                            if '80' in string_genre and q == "crime":
                                print(j)
                                crime.write(j)
                                crime.write("\n")
                            if '10402' in string_genre and q == "music":
                                print(j)
                                music.write(j)
                                music.write("\n")
                            if '9648' in string_genre and q == "mystery":
                                print(j)
                                mystery.write(j)
                                mystery.write("\n")
                            if '10749' in string_genre and q == "romance":
                                print(j)
                                romance.write(j)
                                romance.write("\n")
                            if '878' in string_genre and q == "scifi":
                                print(j)
                                scifi.write(j)
                                scifi.write("\n")
                            if '27' in string_genre and q == "horror":
                                print(j)
                                horror.write(j)
                                horror.write("\n")
                            if '53' in string_genre and q == "thriller":
                                print(j)
                                thriller.write(j)
                                thriller.write("\n")
                            if '37' in string_genre and q == "western":
                                print(j)
                                western.write(j)
                                western.write("\n")
                            if '12' in string_genre and q == "adventures":
                                print(j)
                                adventure.write(j)
                                adventure.write("\n")
                            #print(j)
                    else:
                        print(j + "is not in the Database")
'''
Xinit = 0.02*self.width
Yinit = 0.16*self.height
Xchange = 0.16*self.width
Ychange = 0.2*self.height
XinitText = Xinit + 0.5*Xchange
YinitText = Yinit + 0.5*Ychange
'''
def mouseClick(win, click):
    x = click.getX()
    y = click.getY()
    Xinit = 0.02*win.getWidth()
    Yinit = 0.16*win.getHeight()
    Xchange = 0.16 * win.getWidth()
    Ychange = 0.2 * win.getHeight()
    XinitText = Xinit + 0.5 * Xchange
    YinitText = Yinit + 0.5 * Ychange

    if(Xinit < x < Xinit + Xchange and Yinit < y < Yinit + Ychange):
        app(win, "action")
        return False
    if(Xinit + Xchange < x < Xinit + 2*Xchange and Yinit < y < Yinit + Ychange):
        app(win, "comedy")
        return False
    if(Xinit + 2*Xchange < x < Xinit + 3*Xchange and Yinit < y < Yinit + Ychange):
        app(win, "adventure")
        return False
    if(Xinit + 3*Xchange < x < Xinit + 4*Xchange and Yinit < y < Yinit + Ychange):
        app(win, "animation")
        return False
    if(Xinit + 4*Xchange < x < Xinit + 5*Xchange and Yinit < y < Yinit + Ychange):
        app(win, "documentary")
        return False
    if(Xinit + 5*Xchange < x < Xinit + 6*Xchange and Yinit < y < Yinit + Ychange):
        app(win, "horror")
        return False
    if (Xinit < x < Xinit + Xchange and Yinit + Ychange < y < Yinit + 2*Ychange):
        app(win, "romance")
        return False
    if (Xinit + Xchange < x < Xinit + 2 * Xchange and Yinit + Ychange < y < Yinit + 2*Ychange):
        app(win, "scifi")
        return False
    if (Xinit + 2 * Xchange < x < Xinit + 3 * Xchange and Yinit + Ychange < y < Yinit + 2*Ychange):
        app(win, "music")
        return False
    if (Xinit + 3 * Xchange < x < Xinit + 4 * Xchange and Yinit + Ychange < y < Yinit + 2*Ychange):
        app(win, "thriller")
        return False
    if (Xinit + 4 * Xchange < x < Xinit + 5 * Xchange and Yinit + Ychange < y < Yinit + 2*Ychange):
        app(win, "western")
        return False
    if (Xinit + 5 * Xchange < x < Xinit + 6 * Xchange and Yinit + Ychange < y < Yinit + 2*Ychange):
        app(win, "adventure")
        return False
    if (Xinit < x < Xinit + Xchange and Yinit + 2*Ychange < y < Yinit + 3*Ychange):
        app(win, "war")
        return False
    if (Xinit + Xchange < x < Xinit + 2 * Xchange and Yinit + 2*Ychange < y < Yinit + 3*Ychange):
        app(win, "crime")
        return False
    if (Xinit + 2 * Xchange < x < Xinit + 3 * Xchange and Yinit + 2*Ychange < y < Yinit + 3*Ychange):
        app(win, "fantacy")
        return False
    if (Xinit + 3 * Xchange < x < Xinit + 4 * Xchange and Yinit + 2*Ychange < y < Yinit + 3*Ychange):
        app(win, "family")
        return False
    if (Xinit + 4 * Xchange < x < Xinit + 5 * Xchange and Yinit + 2*Ychange < y < Yinit + 3*Ychange):
        app(win, "drama")
        return False
    if (Xinit + 5 * Xchange < x < Xinit + 6 * Xchange and Yinit + 2*Ychange < y < Yinit + 3*Ychange):
        app(win, "mystery")
        return False
    else:
        pass

#create a window
win = GenreWindow(500, 1000, 0)
window = win.drawWindow()
bool = True
while bool:
    click = window.checkMouse()
    if(click!=None):
        bool = mouseClick(window, click)
lst = ["Movie 1","Movie could be this long", "she", "might be this long too", "It works", "baam", "this was fast", "not that hard", "gotta go to django quick", "gotta get done with this ASAP","sfg","asdfsd","asdfs","asdfsd","sdfsd","sdfs","adsfs","asdfs","sadfsa","fdghf","werttwe","ghjfh","asdf","wertew","nmghn","cvbcv","cvcvb"]
win.drawBlankSheet(lst)
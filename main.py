import os
import re
import requests
from tkinter import *

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

root = Tk()

root.title("Movie Recommender")

intro = Label(root, text = "Hello there!")
intro2 = Label(root, text = "What kind of movie would you like to see today?")
intro.grid(row = 1, column = 0, columnspan = 4)
intro2.grid(row = 2, sticky = W, columnspan = 4)
comedybtn = Button(root, text = "comedy")
actionbtn = Button(root, text = "action")
animationbtn = Button(root, text = "animation")
adventurebtn = Button(root, text = "adventure")
horrorbtn = Button(root, text = "horror")
romancebtn = Button(root, text = "romance")
thrillerbtn = Button(root, text = "thriller")
musicbtn = Button(root, text = "music")
scifibtn = Button(root, text = "scifi")
westernbtn = Button(root, text = "western")
warbtn = Button(root, text = "war")
crimebtn = Button(root, text = "crime")
fantasybtn = Button(root, text = "fantasy")
familybtn = Button(root, text = "family")
documentarybtn = Button(root, text = "documentary")
historybtn = Button(root, text = "history")

intro = Label(root, text="Hello there!")
intro2 = Label(root, text="What kind of movie would you like to see today?")
intro.grid(row=1, column=0, columnspan=4)
intro2.grid(row=2, sticky=W, columnspan=4)

comedybtn.grid(row=3, column=0, sticky=W)
actionbtn.grid(row=3, column=1, sticky=W)
adventurebtn.grid(row=3, column=2, sticky=W)
animationbtn.grid(row=3, column=3, sticky=W)
scifibtn.grid(row=3, column=4, sticky=W)
horrorbtn.grid(row=4, column=0, sticky=W)
romancebtn.grid(row=4, column=1, sticky=W)
thrillerbtn.grid(row=4, column=2, sticky=W)
warbtn.grid(row=4, column=3, sticky=W)
crimebtn.grid(row=4, column=4, sticky=W)
musicbtn.grid(row=5, column=0, sticky=W)
familybtn.grid(row=5, column=1, sticky=W)
fantasybtn.grid(row=5, column=2, sticky=W)
westernbtn.grid(row=5, column=3, sticky=W)
documentarybtn.grid(row=5, column=4, sticky=W)
#root.mainloop()


for root, dirs, files in os.walk(r"C:\\users\\yeab\\desktop\\project\\movies for project"):
    for file in files:
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
                j = file[0:file.index("2")]

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
                        print("Sorry, I do not know the Genre of this movie")
                    else:
                        #print(jsonobj['results'][0]['genre_ids'])
                        string_genre = str(jsonobj['results'][0]['genre_ids'])
                        x = ''.join(string_genre)
                        #print(x)
                        def ACTION():
                            if '28' in string_genre:
                                print(j)
                                action.write(j)
                                action.write("\n")
                        def ANIMATION():
                            if '16' in string_genre:
                                print(j)
                                animation.write(j)
                                animation.write("\n")
                        def DOCUMENTARY():
                            if '99' in string_genre:
                                print(j)
                                documentary.write(j)
                                documentary.write("\n")
                        def DRAMA():
                            if '18' in string_genre:
                                print(j)
                                drama.write(j)
                                drama.write("\n")
                        def FAMILY():
                            if '10751' in string_genre:
                                print(j)
                                family.write(j)
                                family.write("\n")
                        def FANTASY():
                            if '14' in string_genre:
                                print(j)
                                fantacy.write(j)
                                fantacy.write("\n")
                        def HISTORY():
                            if '36' in string_genre:
                                print(j)
                                history.write(j)
                                history.write("\n")
                        def COMEDY():
                            if '35' in string_genre:
                                print(j)
                                comedy.write(j)
                                comedy.write("\n")
                        def WAR():
                            if '10752' in string_genre:
                                print(j)
                                war.write(j)
                                war.write("\n")
                        def CRIME():
                            if '80' in string_genre:
                                print(j)
                                crime.write(j)
                                crime.write("\n")
                        def MUSIC():
                            if '10402' in string_genre:
                                print(j)
                                music.write(j)
                                music.write("\n")
                        def MYSTERY():
                            if '9648' in string_genre:
                                print(j)
                                mystery.write(j)
                                mystery.write("\n")
                        def ROMANCE():
                            if '10749' in string_genre:
                                print(j)
                                romance.write(j)
                                romance.write("\n")
                        def SCIFI():
                            if '878' in string_genre:
                                print(j)
                                scifi.write(j)
                                scifi.write("\n")
                        def HORROR():
                            if '27' in string_genre:
                                print(j)
                                horror.write(j)
                                horror.write("\n")
                        def THRILLER():
                            if '53' in string_genre:
                                print(j)
                                thriller.write(j)
                                thriller.write("\n")
                        def WESTERN():
                            if '37' in string_genre:
                                print(j)
                                western.write(j)
                                western.write("\n")
                        def ADVENTURE():
                            if '12' in string_genre:
                                print(j)
                                adventure.write(j)
                                adventure.write("\n")

                        #print(j)
                else:
                    print(j + "is not in the Database")
                comedybtn.config(command = COMEDY)
                actionbtn.config(command = ACTION)
                adventurebtn.config(command = ADVENTURE)
                animationbtn.config(command = ANIMATION)
                horrorbtn.config(command = HORROR)
                musicbtn.config(command = MUSIC)
                romancebtn.config(command = ROMANCE)
                documentarybtn.config(command = DOCUMENTARY)
                thrillerbtn.config(command = THRILLER)
                warbtn.config(command = WAR)
                crimebtn.config(command = CRIME)
                fantasybtn.config(command = FANTASY)
                scifibtn.config(command = SCIFI)
                westernbtn.config(command = WESTERN)
                historybtn.config(command = HISTORY)

root.mainloop()
                #mn.write(j)
                #mn.write("\n")"""
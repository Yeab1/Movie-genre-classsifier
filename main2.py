import os
import re
import requests

#apikey = 08d24012d752c9e551f35a3516460668
q = input("What kind of movie would you like to watch?")
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
mystery = open("drama.txt", "w")

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

                #mn.write(j)
                #mn.write("\n")"""
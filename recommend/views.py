from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
import os,math
from django.conf import settings
settings.BASE_DIR
from django.core.files import File
from .models import User,snap,logo,movies
import cv2
import smtplib
from email.mime.text import MIMEText
import string,random
from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
import argparse
import sys
import json




def clear(request):
    movieset=movies.objects.all()
    i=0
    for movie in movieset:
        i=i+1
        if i>1101:
            movie.delete()
    return HttpResponse("hello")

def images(request):



    alpha=request.POST['submit']
    """f = open('urlmovie.txt', encoding="utf8")
    myfile = File(f)
    list=[]
    next = myfile.readline()
    while next != "":
        list.append(next)
        next = myfile.readline()


    f = open('ju.txt', encoding="utf8")
    myfile = File(f)
    books = {}
    names = []
    next = myfile.readline()
    while next != "":
        # wordList = re.sub("[^\w]", "|", next).split()
        wordList = next.split("|")
        names.append(wordList[1])
        next = myfile.readline()

    #movies.objects.all().delete()
    for i in range(1601,1682):
        movie=movies(name=names[i],url=list[i])
        movie.save()"""

    list=[]
    mymovies=movies.objects.all()
    for x in mymovies:
        if x.name.startswith(alpha or alpha.lower()):
            list.append(x)
    return render(request, 'recommend/movieimages.html', {'alpha':alpha,'list':list})

def searchmoviebyalphabet(request):
    return render(request, 'recommend/alphabet.html', {})

def meet_the_team(request):
    return render(request, 'recommend/meet_the_team.html', {})


def authenticate(request):
    id=-1
    return render(request, 'recommend/authenticate.html', {'id':id})

def process(request):
    s = request.POST['rated']
    return render(request, 'recommend/allmovies.html', {'s':s})

def newuser(request):
    u = get_object_or_404(User, pk=1)
    u.count+=1
    u.save()
    return render(request, 'recommend/authenticate.html', {'id': u.count,'count':-1})

def takeimage(request):

    sn=snap()
    sn.name="me12"



    # Camera 0 is the integrated web cam on my netbook
    camera_port = 0

    # Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 30

    # Now we can initialize the camera capture object with the cv2.VideoCapture class.
    # All it needs is the index to a camera port.
    camera = cv2.VideoCapture(camera_port)

    # Captures a single image from the camera and returns it in PIL format
    def get_image():
        # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = camera.read()
        return im

    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in range(ramp_frames):
        temp = get_image()
    print("Taking image...")
    # Take the actual image we want to keep
    camera_capture = get_image()
    file = "media/chgab"+str(int(random.random()*1000))+".png"
    # A nice feature of the imwrite method is that it will automatically choose the
    # correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, camera_capture)
    sn.file=file
    sn.save()
    # You'll want to release the camera, otherwise you won't be able to create a new
    # capture object until your script exits
    del (camera)
    u = get_object_or_404(User, pk=1)

    return render(request, 'recommend/first.html', {'cnt': u.count,})


def polo(request):
    rate = request.POST['star']
    return HttpResponse("what is "+rate)


def rate(request):
    user_id = request.POST['user']
    u = get_object_or_404(User, pk=1)
    if int(user_id)>u.count:
        return render(request, 'recommend/authenticate.html', {'count': u.count,'id':int(user_id)})
    """f = open('ju.txt', encoding="utf8")
    myfile = File(f)
    books = {}
    
    next = myfile.readline()
    while next != "":
        # wordList = re.sub("[^\w]", "|", next).split()
        wordList = next.split("|")
        wordList = [wordList[0], wordList[1]]
        books[wordList[0]] = wordList[1]
        next = myfile.readline()
    for item in books.keys():
        list.append(books[item])"""
    list = []
    mov=movies.objects.all()
    for m in mov:
        list.append(m.name)

    context={'list':list,'user_id':user_id}
    return render(request, 'recommend/rate.html', context)


def index(request):
    u = get_object_or_404(User, pk=1)
    g=get_object_or_404(logo,pk=1)
    template = loader.get_template('recommend/first.html')
    return HttpResponse(template.render({'cnt':u.count,'img':g}, request))

def yesrateit(request):
    user = request.POST['userr']
    movieid=request.POST['movieid']
    rating = 6-int(request.POST['star'])

    f = open('hello.txt', "a", encoding="utf8")
    myfile = File(f)
    myfile.write("\n" + str(user) + " " + str(movieid) + " " + str(rating) + " " + "879270459")
    f.close()
    f = open('ju.txt', encoding="utf8")
    myfile = File(f)
    books = {}
    list = []
    next = myfile.readline()
    while next != "":
        # wordList = re.sub("[^\w]", "|", next).split()
        wordList = next.split("|")
        wordList = [wordList[0], wordList[1]]
        books[wordList[0]] = wordList[1]
        next = myfile.readline()
    for item in books.keys():
        list.append(books[item])

    return render(request, 'recommend/rate.html', {'user_id':user,'list':list})

def help(request):
    movie=movies.objects.get()
    movie.url="https://i.ytimg.com/vi/PFxQKfjCn9E/hqdefault.jpg"
    movie.save()

    """ movieset=movies.objects.all()
    for movie in movieset:
        x=movie.name
        x = x[0:len(x) - 7]
        x = x.lower()
        x = x.replace("&", "and")
        x = re.sub('\(.*\)', '', x)
        x = re.sub(' *$', '', x)
        x = re.sub('[^A-Za-z0-9 ]*', '', x)
        x = re.sub(' *$', '', x)
        x = x.replace(" ", "_")
        x = re.sub('_the$', '', x)
        x = re.sub('_$', '', x)
        x = re.sub('_a$', '', x)
        movie.modifiedname=x
        movie.save()"""
    return HttpResponse("done")

def moviesearch(request):
    movie=request.POST['movie']
    user=request.POST['user']

    list = []
    mov = movies.objects.all()
    for m in mov:
        list.append(m.name)
    """
    f = open('ju.txt', encoding="utf8")
    myfile = File(f)
    books = {}
    list = []
    next = myfile.readline()
    while next != "":
        # wordList = re.sub("[^\w]", "|", next).split()
        wordList = next.split("|")
        wordList = [wordList[0], wordList[1]]
        books[wordList[0]] = wordList[1]
        next = myfile.readline()
    for item in books.keys():
        list.append(books[item])"""
    movieid=1
    flag=0
    moviematched=""
    bestmatch=-1
    guessid=-1
    guessmovie=""

    for mov in list:
        item=mov[0:len(mov)-7]
        item=item.lower()

        if (item).startswith(movie.lower(), 0,len(item)):
            bestmatch=movieid
            moviematched=mov
        if (item[0:int(3*len(item)/4)]==(movie.lower())):
            guessid=movieid
            guessmovie=mov
        if item!=movie.lower():
            movieid=movieid+1
        else:
            flag=1
            break


    if bestmatch==-1 and guessid==-1:
       return render(request, 'recommend/rate.html', {'bestmatch':-1,'guessid':-1,'user_id':user,'list':list,})

    elif bestmatch==-1:
        movieid=guessid
        moviematched=guessmovie
    else:
        movieid=bestmatch




    context = {'movieid': movieid, 'user': user, 'movie': moviematched}
    return render(request, 'recommend/allmovies.html', context)








def loaddata(request):
    u = get_object_or_404(User, pk=1)

    user_id=request.POST['user']
    if int(user_id)>u.count:
        return render(request, 'recommend/first.html', {'user':int(user_id),'cnt':u.count})

    f= open('ju.txt', encoding="utf8")
    myfile=File(f)
    prefs = {}

    import re

    books = {}
    i = 0
   # f = open("static/recommend/ju.txt", encoding="utf8")
    next = myfile.readline()
    while next != "":
        # wordList = re.sub("[^\w]", "|", next).split()
        wordList = next.split("|" or "||")
        wordList = [wordList[0], wordList[1]]
        books[wordList[0]] = wordList[1]
        #remove

        next = myfile.readline()

    #print(books)



    a1 = ""
    a2 = ""
    a3 = ""

    f = open('hello.txt', encoding="utf8")
    myfile = File(f)
    next = myfile.readline()
    while next != "":
        i = 0
        for word in next.split():
            i = i + 1
            if i == 4:
                break
            if i == 1:
                a1 = str(word)
            elif i == 2:
                a2 = str(word)
            else:
                a3 = int(word)

        if (a1 not in prefs):
            prefs[a1] = {}
        if a2=="814":
            print(a1+" "+a2+" "+str(a3))
        prefs[a1][a2] = a3
        next = myfile.readline()

    f.close()

    if user_id not in prefs:
        return render(request, 'recommend/hi.html', {'list':[]})

    # Returns the Pearson correlation coefficient for p1 and p2
    def sim_pearson(prefs, p1, p2):
        # Get the list of mutually rated items
        si = {}
        for item in prefs[p1]:
            if item in prefs[p2]: si[item] = 1
        # Find the number of elements
        n = len(si)
        # if they are no ratings in common, return 0
        if n == 0: return 0
        # Add up all the preferences
        sum1 = sum([prefs[p1][it] for it in si])
        sum2 = sum([prefs[p2][it] for it in si])
        # Sum up the squares
        sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
        sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
        # Sum up the products
        pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
        # Calculate Pearson score
        num = pSum - (sum1 * sum2 / n)
        den = math.sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
        if den == 0: return 0
        r = num / den
        return r
    print (sim_pearson(prefs,"1","13"))
    # Returns the best matches for person from the prefs dictionary.
    # Number of results and similarity function are optional params.
    def topMatches(prefs, person, n=5, similarity=sim_pearson):
        scores = [(similarity(prefs, person, other), other)
                  for other in prefs if other != person]
        # Sort the list so the highest scores appear at the top
        scores.sort()
        scores.reverse()
        return scores[0:n]

    # Gets recommendations for a person by using a weighted average
    # of every other user's rankings
    def getRecommendations(prefs, person, similarity=sim_pearson):
        totals = {}
        simSums = {}
        for other in prefs:
            # don't compare me to myself
            if other == person: continue
            sim = similarity(prefs, person, other)
            # ignore scores of zero or lower
            if sim <= 0: continue
            for item in prefs[other]:
                # only score movies I haven't seen yet
                if item not in prefs[person] or prefs[person][item] == 0:
                    # Similarity * Score
                    totals.setdefault(item, 0)
                    totals[item] += prefs[other][item] * sim
                    # Sum of similarities
                    simSums.setdefault(item, 0)
                    simSums[item] += sim
        # Create the normalized list
        rankings = [(total / simSums[item], item) for item, total in totals.items()]
        # Return the sorted list
        rankings.sort()
        rankings.reverse()
        return rankings

    #print(topMatches(prefs, '945'))
    #print("\n")

    i = 0
    list=[]
    length=len(prefs)
    answers = getRecommendations(prefs,str(user_id))
    #print(answers)



    for item in answers:
        i = i + 1
        if i == 11: break
        list.append(books[item[1]])


    listnew=[]
    for item in list:
        mov=movies.objects.filter(name=item)
        listnew.append(mov[0])
    context = {'list': listnew, }
    return render(request, 'recommend/hi.html', context)


#
def myrating(request):
    return render(request, 'recommend/myrating.html', {})
def ihaverated(request):
    user_id = request.POST['user']
    a1 = ""
    a2 = ""
    a3 = ""
    prefs={}
    f = open('hello.txt', encoding="utf8")
    myfile = File(f)
    next = myfile.readline()
    while next != "":
        i = 0
        for word in next.split():
            i = i + 1
            if i == 4:
                break
            if i == 1:
                a1 = str(word)
            elif i == 2:
                a2 = str(word)
            else:
                a3 = int(word)

        if (a1 not in prefs):
            prefs[a1] = {}

        prefs[a1][a2] = a3
        next = myfile.readline()

    f.close()
    x=prefs[user_id]
    list=[]
    rating=[]
    print(len(prefs['76']))

    for y in x:
        temp=[]
        try:

            temp.append(movies.objects.get(movieid=int(y)));
            #print(movies.objects.get(movieid=int(y)))
            temp.append(x[y])
        except:
            aa=movies.objects.filter(movieid=int(y))
            if len(aa)>0:
                b=aa[0]
                temp.append(b)
                temp.append(x[y])
        list.append(temp)


    return render(request, 'recommend/ihaverated.html', {'list':list})
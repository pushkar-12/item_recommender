#5 1 1.3735057130365123
#5 5 1.3819752510808316
#5 10 1.3341644684790732
#5 20 1.2866523631402507
#5 30 1.254990084082328
#5 40 1.2327675339648496
#5 50 1.204126900360165
#5 60 1.180859739631113
#5 70 1.1633616788832062
#5 80 1.1475208459508033
#5 100 1.1175424723150795
#5 150 1.0576391177392952
#5 200 1.0335167089776724
#5 250 1.0211884438147198
#5 300 1.0150201264436443
#5 350 1.0128673490745586
#5 400 1.0114714739723847
#5 450 1.0115557534086157
#5 500 1.0107412163785325
#5 600 1.010592256033949
#5 700 1.0104865291920584
#5 800 1.0108455185006293
#5 900 1.0108454788898251
#5 942 1.0108454788898251

from django.core.files import File
import math

f = open('C:/Users/hp/Desktop/ItemRecommender/ju.txt', encoding="utf8")
myfile = File(f)
prefs = {}

books = {}
i = 0
# f = open("static/recommend/ju.txt", encoding="utf8")
next = myfile.readline()
while next != "":
    # wordList = re.sub("[^\w]", "|", next).split()
    wordList = next.split("|" or "||")
    wordList = [wordList[0], wordList[1]]
    books[wordList[0]] = wordList[1]
    # remove

    next = myfile.readline()

a1 = ""
a2 = ""
a3 = ""

f = open('C:/Users/hp/Desktop/ItemRecommender/train5.txt', encoding="utf8")
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

    # Returns the best matches for person from the prefs dictionary.
    # Number of results and similarity function are optional params.


def topMatches(prefs, person, n=1, similarity=sim_pearson):
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
    # rankings.sort()
    # rankings.reverse()
    return rankings


# print(topMatches(prefs, '945'))
# print("\n")

i = 0
list = []
length = len(prefs)

"""for user in range(1,944):
    answers=getRecommendations(prefs,str(user))


for x in range(1,100):
    for s in answers:
        if s[1]==str(x):
            print(str(x)+"--"+str(s[0])+"\n")

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

"""
"""
t = 0
prev = 0
ans = 0
shi = []
f = open('C:/Users/hp/Desktop/ItemRecommender/test5.txt', encoding="utf8")
myfile = File(f)
for line in myfile:
    k = line.split('\t')

    if (k[0] != prev):
        shi = getRecommendations(prefs, k[0])
    prev = k[0]
    for l in shi:
        if l[1] == k[1]:
            ans = ans + (l[0] - int(k[2])) * (l[0] - int(k[2]))
            t += 1
            break
print(math.sqrt(ans / t))

print(topMatches(prefs,"1"))
for user in range(1,944):
        
    x=topMatches(prefs,str(user))
    prefso={}
    
    for i in x:
        a=i[1]
        prefso[a]=(prefs[a])

print('\n\n')
print(prefso)
"""

t = 0
prev = 0
ans = 0
shi = []
f = open('C:/Users/hp/Desktop/ItemRecommender/test5.txt', encoding="utf8")
myfile = File(f)
for line in myfile:
    k = line.split('\t')

    if (k[0] != prev):
        x = topMatches(prefs, k[0])

        prefso = {}

        for i in x:
            a = i[1]
            prefso[a] = (prefs[a])
        prefso[k[0]]=prefs[k[0]]
        shi = getRecommendations(prefso, k[0])
    prev = k[0]
    for l in shi:
        if l[1] == k[1]:
            ans = ans + (l[0] - int(k[2])) * (l[0] - int(k[2]))
            t += 1
            break
print(math.sqrt(ans / t))
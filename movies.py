

def readMovieFiles(fileName):
    filePointer=open(fileName)
    lines = filePointer.readlines()
    genreFile=open("genre.data")
    genreLines = genreFile.readlines()
    genreMap = {}
    for line in genreLines:
        line = line.split("|")
        genreMap[int(line[1])] = line[0]
       
    # print genreMap
    
    movieMap={}
    for line in lines:
        #print line.split("|")
        movieLine = line.split("|")
        movieLine.remove("")
        movieId=(movieLine[0])
        movieMap[movieId]={}
        movieMap[movieId]={"movieName":movieLine[1],"releaseDate" : movieLine[2],"url" : movieLine[3],"genre":list(),"totalRating":0,"totalCount": 0,"average":0}
        genreIndex=4;
        while(genreIndex<23):
            # print line[genreIndex]
            # print line
            if(int(movieLine[genreIndex]) == 1):
            # print genreIndex
                movieMap[movieId]["genre"].append(genreMap.get(genreIndex-4))
            genreIndex=genreIndex+1
    return movieMap    
    #print movieMap
        
def readRatingFile(ratingfile):
    rating = open(ratingfile,'r')
    line = rating.readline()
    rateMap=[]
    while line:    
        value = line.split('\t')
        rateMap.append({'userId':value[0],'movieId':value[1],'rating':int(value[2])})
        line = rating.readline()
    return rateMap 
        
   
   
def readUserFile(userfile):
    user = open(userfile,'r')
    line = user.readline()
    userMap={}
    while line:    
        value = line.split('|')
#         print value[1]
        userMap[value[0]]={'userId':value[0] , "age" : value[1],"gender" : value[2],"profession":value[3],"timestamp" : value[4],"totalCount":0}
        line = user.readline()
    return userMap 
    
def mostActiveUser(userMap): 
    maxItem = max(item['totalCount'] for item in userMap.values())
    for users in userMap.values():
        if(users['totalCount']==maxItem):
            print "Most Active User"
            print users['userId']

def MostWatchedMovie(movieMap):
    maxItem = max(item['totalCount'] for item in movieMap.values())
    for movies in movieMap.values():
        if(movies['totalCount']==maxItem):
            print "\nMost watched Movie"
            print movies['movieName']
    
def highestRatedGenre(movieMap):
    for movies in movieMap.keys():
        movieMap.get(movies)["average"]=float(movieMap.get(movies)["totalRating"] )/ float(movieMap.get(movies)["totalCount"])
        #print float(movieMap.get(movies)["average"])
    maxItem = max(float(item['average']) for item in movieMap.values())
    
    for movies in movieMap.values():
        if(float(movies['average'])==maxItem):
            print "\nhighest Rated genre"
            print movies['genre']
            break
        
def topMovieByGenre(movieMap):

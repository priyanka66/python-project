import movies
movieMap=movies.readMovieFiles("movie.data")
rateMap=movies.readRatingFile("ratings.data")
userMap=movies.readUserFile("user.data")

#print rateMap

for rate in rateMap:
    movie = movieMap.get(rate['movieId'])
    movie['totalCount'] = movie['totalCount'] + 1
    movie['totalRating'] = rate['rating'] + movie['totalRating']
    # print movie['totalRating']
    user = userMap.get(rate['userId'])
    user['totalCount']=user['totalCount'] + 1
    
movies.mostActiveUser(userMap)
movies.MostWatchedMovie(movieMap) 
movies.highestRatedGenre(movieMap)
movies.topMovieByGenre(movieMap)


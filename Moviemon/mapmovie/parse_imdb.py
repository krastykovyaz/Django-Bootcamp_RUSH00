#!/usr/bin/python3
import random
import imdb

def get_person(persons):
    if not persons:
        return None
    person = list()
    for p in persons:
        person.append(p['name'])
    return person


def get_moviemons(amount=10):
    '''
    amount - max number of movies
    return - dictionary  {'MovieID' : 
    {'name', 'poster', 'director', 'year', 'rating', 'synopsis', 'actors'}}
    director and actors - are list.
    '''
    ia = imdb.IMDb()
    keywords = ia.search_keyword('monster')
    i = 0
    moviemons = dict()
    while len(moviemons) < amount + 1:
        keyword = random.choice(keywords)
        movies = ia.get_keyword(keyword)
        for i in range(len(movies)):
            if movies[i]:
                if not moviemons.get(movies[i].movieID):
                    movie = ia.get_movie(movies[i].movieID)
                    director = get_person(movie.get('director'))
                    actors = get_person(movie.get('actors'))
                    if movie.get('plot'):
                        synopsis = movie.get('plot')[0]
                    else:
                        synopsis = None
                    year = movie.get('year')
                    poster = movie.get('cover url')
                    if movie.get('rating'):
                        moviemons[movies[i].movieID] =\
                            {'name': movies[i]['title'], 
                            'poster' : poster,
                            'director' : director,
                            'year' : year,
                            'rating': movie.get('rating'),
                            'synopsis': synopsis,
                            'actors': actors}
                        break
    return(moviemons)


# if __name__ == '__main__':
#     print(get_moviemons(3))
#    ia = imdb.IMDb()
#    movie = ia.get_movie('0133093')
#    print(movie.infoset2keys)
#    print(movie.get)

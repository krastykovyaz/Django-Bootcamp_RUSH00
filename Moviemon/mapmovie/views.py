from django.shortcuts import render
from django.http import HttpResponse
from . forms import MovieForm
from . game_data import GameData
from . parse_imdb import get_moviemons
from django.conf import settings
import random, os
from time import sleep

def NewGame(request):
    return render(request, 'mapmovie/new_game.html')

g = GameData()
# print(params)

def StartGame(request):
    films_10 = []
    # if os.path.isfile(settings.FT_GAMEFILE):
    #     g.load()
    # else:
    g.load_default_settings()
    params = g.data.get('movies')
    for k, v in params.items():
        films_10.append(v['name'])
    box_movies = []
    params_2 = g.data.get('movies_caught')
    for k, v in params_2.items():
        print(k, '-----------', v)
        box_movies.append(v['name'])
    # box_movies = g.data['movies_caught']
    # print(films_10)
    return render(request, 'mapmovie/choose_pos.html', {'films': films_10, 'box_movies': box_movies})

def KickBall():
    locations = ['s', 'n', 'w', 'e', 's_w', 's_e', 'n_w', 'n_e']
    return random.choice(locations)


def grab_monster():
    m_ID = g.get_random_movie()
    g.move_to_caught(m_ID)
    print("m_ID", m_ID)
    g.dump()




def StepAhead(request):
    ball_loc = KickBall()
    films_10 = []
    g.load()
    params = g.data.get('movies')
    for k, v in params.items():
        films_10.append(v['name'])
    go_to = str()
    if request.method == 'GET':
        if 'n_e' in str(request):
            return render(request, f"mapmovie/{str(request).split('/')[-1][:-5]}.html")
        return render(request, f"mapmovie/{str(request).split('/')[-2][:-3]}.html")
    try:
        if request.method == 'POST':
            if "step" in request.POST:
                go_to = request.POST.get('step')
    except:
        print("Something went wrong !")
    print(ball_loc, go_to)
    if go_to == ball_loc:
        grab_monster()
    g.load()
    params = g.data.get('movies')
    if not params:
        return index(request)
    # data_movie = set_param(pos)
    box_movies = []
    params_2 = g.data.get('movies_caught')
    for k, v in params_2.items():
        # print(k, '-----------', v)
        box_movies.append(v['name'])
    if go_to == '':
        return render(request, f'mapmovie/c_doll.html')
    return render(request, f'mapmovie/{go_to}_doll.html', {'ball': ball_loc, 'films': films_10, 'box_movies': box_movies})


def StartPos(request):
    return render(request, 'mapmovie/c_doll.html')


def index(request):
#    g = game_data.GameData()
#    g = g.load_default_settings()


#    m_ID = g.get_random_movie()
#    g.move_to_caught(m_ID)
#    m_ID = g.get_random_movie()
#    g.move_to_caught(m_ID)
    sleep(3)
    return render(request, 'mapmovie/index.html',
    {'movies' : g.data['movies_caught'],}, )
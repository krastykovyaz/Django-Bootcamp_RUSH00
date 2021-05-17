from django.urls import path
from . import views

urlpatterns = [
    path('s_doll_id/', views.StepAhead, name='s_doll'),
    path('n_doll_id/', views.StepAhead, name='n_doll'),
    path('w_doll_id/', views.StepAhead, name='w_doll'),
    path('e_doll_id/', views.StepAhead, name='e_doll'),
    path('c_doll_id/', views.StepAhead, name='c_doll'),
    path('s_w_doll_id/', views.StepAhead, name='s_w_doll'),
    path('s_e_doll_id/', views.StepAhead, name='s_e_doll'),
    path('n_w_doll_id/', views.StepAhead, name='n_w_doll'),
    path('n_e_doll_id', views.StepAhead, name='n_e_doll'),
    path('c_doll_id/', views.StartPos, name='c_doll'),
    path('', views.NewGame, name='new_game'),
    path('start_game/', views.StartGame, name='start_game'),
    path('result/', views.index, name='index')
]

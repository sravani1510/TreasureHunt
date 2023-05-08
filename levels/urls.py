from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/',views.about,name='about'),
    path('level1/',views.level1,name='level1'),
    path('level2/',views.level2,name='level2'),
    path('level3/',views.level3,name='level3'),
    path('level4/',views.level4,name='level4'),
    path('level5/',views.level5,name='level5'),
    path('level5a/',views.level5a,name='level5a'),
    path('level6/',views.level6,name='level6'),
    path('level7/',views.level7,name='level7'),
    path('level8/',views.level8,name='level8'),
    path('game_over/', views.game_over, name='game_over'),
    path('final/',views.final,name="final"),
    path('treasurehunt_list/',views.treasurehunt_list,name="treasurehunt_list"),

    
]
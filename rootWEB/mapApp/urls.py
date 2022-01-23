
from django.contrib import admin
from django.urls import path
from mapApp import views

urlpatterns = [
    # http://127.0.0.1:8000/map/main
    path('main/' , views.about , name = "main") ,

    # map
    path('map/' , views.map , name = "map") ,
    path('map_zerowaste/' , views.map_zerowaste , name = "map_zerowaste") ,
    path('map_vegan/' , views.map_vegan , name = "map_vegan") ,

    # zerowaste_data
    path('zerowaste_data_all/' , views.zerowaste_data_all , name="zerowaste_data_all") ,
    path('zerowaste_membership/' , views.zerowaste_membership , name="zerowaste_membership") ,
    path('zerowaste_data/' , views.zerowaste_data , name = "zerowaste_data") ,
    path('zerowaste_data_refill/' , views.zerowaste_data_refill , name="zerowaste_data_refill") ,
    path('zerowaste_data_recycle/' , views.zerowaste_data_recycle , name="zerowaste_data_recycle") ,
    path('zerowaste_data_etc/' , views.zerowaste_data_etc , name="zerowaste_data_etc") ,

    # vegan_data
    path('vegan_data_all/' , views.vegan_data_all , name = "vegan_data_all" ) ,
    path('vegan_membership/' , views.vegan_membership , name="vegan_membership") ,
    path('vegan_data_kor/' , views.vegan_data_kor , name="vegan_data_kor") ,
    path('vegan_data_wes/' , views.vegan_data_wes , name="vegan_data_wes") ,
    path('vegan_data_chi/' , views.vegan_data_chi , name="vegan_data_chi") ,
    path('vegan_data_jap/' , views.vegan_data_jap , name="vegan_data_jap") ,
    path('vegan_data_cafe/' , views.vegan_data_cafe , name="vegan_data_cafe") ,
    path('vegan_data_bake/' , views.vegan_data_bake , name="vegan_data_bake") ,
    path('vegan_data_etc/' , views.vegan_data_etc , name="vegan_data_etc") ,

    # user
    path('login/' , views.login , name = "login") , # 회원가입
    path('logout/' , views.logout , name = "logout") ,
    path('join/' , views.join , name = "join") ,
    path('registerForm/' , views.registerForm , name = "registerForm") ,

    # board
    path('board/' , views.board , name = "board") ,
    # path('news_read/' , views.news_read , name = "news_read") ,

    # load data
    path('CsvToModel/', views.CsvToModel, name="CsvToModel"),
]

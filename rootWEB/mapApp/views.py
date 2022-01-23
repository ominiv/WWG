import chardet
import numpy as np
import pandas as pd
from django.http import JsonResponse , HttpResponse , HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.conf import settings

# Login에 이용되는 Module
import csv
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
from django.contrib import auth

# Create your views here.

z_path = 'C:/Users/user/PJT/WWG/rootWEB/mapApp/db/Zerowaste.csv'
zerowaste_df = pd.read_csv(z_path , encoding='UTF-8')
zerowaste_df = zerowaste_df.replace(np.NaN , 0)

v_path = 'C:/Users/user/PJT/WWG/rootWEB/mapApp/db/Veganfood.csv'
vegan_df = pd.read_csv(v_path , encoding='UTF-8')
vegan_df = vegan_df.replace(np.NaN , 0)
vegan_df.rename(columns={'설명(판매메뉴)': '설명'} , inplace= True)
vegan_df.rename(columns={'위도 ': '위도'} , inplace= True)

# About page - main page
#[TEST] 로그인 할경우 UserID 뽑아보기
def about(request) :
    print('mapApp about index ~ ')
    myuser = request.session.get('user')
    if myuser:
        # user = WwgUser.objects.get(user_id=myuser)
        user = myuser
        return render(request, 'map/about.html', {'user_id': user})
    return render(request, 'map/about.html')


# Map page - 완료
# main map
from ast import literal_eval
def map(request):
    print('mapApp map index ~ ')
    myuser = request.session.get('user')
    if myuser:
        user = myuser
        recomm = WwgUserRecomm.objects.filter(user_id=user).values()
        v_recomm = [];
        z_recomm = [];
        top_recomm = [];
        top_score = []
        # Vegan Recommand list
        print('Vegan Recommand list')
        print(literal_eval(recomm[0]['vegan_recomm']).keys());
        for place in literal_eval(recomm[0]['vegan_recomm']).keys():
            row = WwgVegan.objects.filter(index=place).values()
            print(place, ':', row[0]['name'], round(row[0]['WWGScore'], 2))
            # row[0]['WWGScore'] = round(row[0]['WWGScore'],2)
            v_recomm.append(row[0])
        # Zero Recommand list
        print('Zerowaste Recommand list')
        print(literal_eval(recomm[0]['zerowaste_recomm']).keys());
        for place in literal_eval(recomm[0]['zerowaste_recomm']).keys():
            row = WwgZerowaste.objects.filter(index=place).values()
            print(place, ':', row[0]['name'], round(row[0]['WWGScore'], 2))
            # row[0]['WWGScore'] = round(row[0]['WWGScore'],2)
            # print(row[0]['WWGScore'])
            z_recomm.append(row[0])
        # ---TopPlace
        print('TopPlace list')
        Toprecomm = TopPlace.objects.all().values()
        print(literal_eval(Toprecomm[0]['TopVegan'])[0].keys());
        print(literal_eval(Toprecomm[0]['TopZerowaste'])[0].keys());
        for place in literal_eval(Toprecomm[0]['TopVegan'])[0].keys():
            row = WwgVegan.objects.filter(index=place).values()
            print(place, ':', row[0]['name'], round(row[0]['WWGScore'], 2))
            # row[0]['WWGScore'] = round(row[0]['WWGScore'],2)
            # print(row[0]['WWGScore'])
            top_recomm.append(row[0])
        for place in literal_eval(Toprecomm[0]['TopZerowaste'])[0].keys():
            row = WwgZerowaste.objects.filter(index=place).values()
            print(place, ':', row[0]['name'], round(row[0]['WWGScore'], 2))
            # row[0]['WWGScore'] = round(row[0]['WWGScore'],2)
            # print(row[0]['WWGScore'])
            top_recomm.append(row[0])
        for score in literal_eval(Toprecomm[0]['TopVegan'])[0].values():
            top_score.append(round(score, 2))
        for score in literal_eval(Toprecomm[0]['TopZerowaste'])[0].values():
            top_score.append(round(score, 2))

        return render(request, 'map/map_loginmain.html', {'user_id': user,
                                                            'v_recomm_0': v_recomm[0], 'v_recomm_1': v_recomm[1],
                                                            'v_recomm_2': v_recomm[2],
                                                            'z_recomm_0': z_recomm[0], 'z_recomm_1': z_recomm[1],
                                                            'z_recomm_2': z_recomm[2],
                                                            'top_recomm_0': top_recomm[0], 'top_recomm_1': top_recomm[1],
                                                            'top_recomm_2': top_recomm[2],
                                                            'top_recomm_3': top_recomm[3], 'top_recomm_4': top_recomm[4],
                                                            'top_recomm_5': top_recomm[5],
                                                            'top_score_0': top_score[0], 'top_score_1': top_score[1],
                                                            'top_score_2': top_score[2],
                                                            'top_score_3': top_score[3], 'top_score_4': top_score[4],
                                                            'top_score_5': top_score[5], })
    else:
        top_recomm = [];
        top_score = []
        # ---TopPlace
        print('TopPlace list')
        Toprecomm = TopPlace.objects.all().values()
        print(literal_eval(Toprecomm[0]['TopVegan'])[0].keys());
        print(literal_eval(Toprecomm[0]['TopZerowaste'])[0].keys());
        for place in literal_eval(Toprecomm[0]['TopVegan'])[0].keys():
            row = WwgVegan.objects.filter(index=place).values()
            print(place, ':', row[0]['name'], round(row[0]['WWGScore'], 2))
            # row[0]['WWGScore'] = round(row[0]['WWGScore'],2)
            # print(row[0]['WWGScore'])
            top_recomm.append(row[0])
        for place in literal_eval(Toprecomm[0]['TopZerowaste'])[0].keys():
            row = WwgZerowaste.objects.filter(index=place).values()
            print(place, ':', row[0]['name'], round(row[0]['WWGScore'], 2))
            # row[0]['WWGScore'] = round(row[0]['WWGScore'],2)
            # print(row[0]['WWGScore'])
            top_recomm.append(row[0])
        for score in literal_eval(Toprecomm[0]['TopVegan'])[0].values():
            top_score.append(round(score, 2))
        for score in literal_eval(Toprecomm[0]['TopZerowaste'])[0].values():
            top_score.append(round(score, 2))
        return render(request, 'map/map_main.html',
                        {'top_recomm_0': top_recomm[0], 'top_recomm_1': top_recomm[1], 'top_recomm_2': top_recomm[2],
                        'top_recomm_3': top_recomm[3], 'top_recomm_4': top_recomm[4], 'top_recomm_5': top_recomm[5],
                        'top_score_0': top_score[0], 'top_score_1': top_score[1], 'top_score_2': top_score[2],
                        'top_score_3': top_score[3], 'top_score_4': top_score[4], 'top_score_5': top_score[5], })

# zerowaste map
def map_zerowaste(request) :
    print('mapApp map_zerowaste index ~ ')
    myuser = request.session.get('user')
    if myuser:
        user = WwgUser.objects.get(user_id=myuser)
        return render(request, 'map/map_zerowaste.html', {'user_id': user})
    return render(request , 'map/map_zerowaste.html')

# vegan map
def map_vegan(request) :
    print('mapApp map_vegan index ~ ')
    myuser = request.session.get('user')
    if myuser:
        user = WwgUser.objects.get(user_id=myuser)
        return render(request, 'map/map_vegan.html', {'user_id': user})
    return render(request , 'map/map_vegan.html')


# data path
# zerowaste data - 완료
# 전체
def zerowaste_data_all(request) :
    print('mapApp zerowaste all index ~')

    zerowasteList = []
    for idx in zerowaste_df.index :
        zerowasteList.append({
            'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
            'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
            'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
            'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
            'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
            'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
            'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
            'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
            'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
            'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() , # numpy
            'WWGScore' : (zerowaste_df.iloc[idx , : ].WWGScore).tolist() , # numpy
            'recomm' : zerowaste_df.iloc[idx , : ].추천장소 ,
        })
    print('zerowasteList all complete!!')

    return JsonResponse(zerowasteList, safe=False)

# 멤버쉽
def zerowaste_membership(request) :
    print('mapApp zerowaste membership index ~')
    zerowaste_sample_df = zerowaste_df.sample(n=10)
    zerowaste_membership_df = zerowaste_sample_df.reset_index()

    zerowasteList = []
    for idx in zerowaste_membership_df.index :
        zerowasteList.append({
            'id' : (zerowaste_membership_df.iloc[idx ,  : ].번호).tolist() , # numpy
            'name' : zerowaste_membership_df.iloc[idx ,  : ].상호명 ,
            'number' : zerowaste_membership_df.iloc[idx ,  : ].전화번호 ,
            'address' : zerowaste_membership_df.iloc[idx ,  : ].소재지 ,
            'category' : zerowaste_membership_df.iloc[idx ,  : ].업종 ,
            'about' : zerowaste_membership_df.iloc[idx ,  : ].설명 ,
            'imgURL' : zerowaste_membership_df.iloc[idx ,  : ].imgUrl ,
            'img' : zerowaste_membership_df.iloc[idx ,  : ].jpg ,
            'lat' : (zerowaste_membership_df.iloc[idx ,  : ].위도).tolist() , # numpy
            'lng' : (zerowaste_membership_df.iloc[idx ,  : ].경도).tolist() , # numpy
            'WWGScore': (zerowaste_membership_df.iloc[idx, :].WWGScore).tolist(),  # numpy
            'recomm': zerowaste_membership_df.iloc[idx, :].추천장소,
        })
    print('zerowasteList all complete!!')

    return JsonResponse(zerowasteList, safe=False)

# 제로웨이스트
def zerowaste_data(request) :
    print('mapApp zerowaste index ~')
    print(zerowaste_df.head(5))

    zerowasteList = []
    for idx in zerowaste_df.index :
        if zerowaste_df.iloc[idx , 4] == '제로웨이스트샵' or zerowaste_df.iloc[idx , 4] == '리필샵 , 제로웨이스트샵':
            zerowasteList.append({
                'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
                'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
                'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
                'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
                'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
                'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
                'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
                'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
                'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
                'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() , # numpy
                'WWGScore': (zerowaste_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': zerowaste_df.iloc[idx, :].추천장소,
            })
    print('zerowasteList complete!!')

    return JsonResponse(zerowasteList, safe=False)

# 리필샵
def zerowaste_data_refill(request) :
    print('mapApp zerowaste refill index ~')

    zerowasteList = []
    for idx in zerowaste_df.index :
        if zerowaste_df.iloc[idx , 4] == '리필샵' or zerowaste_df.iloc[idx , 4] == '리필샵 , 제로웨이스트샵':
            zerowasteList.append({
                'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
                'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
                'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
                'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
                'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
                'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
                'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
                'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
                'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
                'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() , # numpy
                'WWGScore': (zerowaste_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': zerowaste_df.iloc[idx, :].추천장소,
            })
    print('zerowasteList refill complete!!')

    return JsonResponse(zerowasteList, safe=False)

# 다회용기
def zerowaste_data_recycle(request) :
    print('mapApp zerowaste recycle index ~')

    zerowasteList = []
    for idx in zerowaste_df.index :
        if zerowaste_df.iloc[idx , 4] == '다회용기' :
            zerowasteList.append({
                'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
                'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
                'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
                'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
                'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
                'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
                'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
                'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
                'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
                'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() , # numpy
                'WWGScore': (zerowaste_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': zerowaste_df.iloc[idx, :].추천장소,
            })
    print('zerowasteList recycle complete!!')

    return JsonResponse(zerowasteList, safe=False)

# 기타
def zerowaste_data_etc(request) :
    print('mapApp zerowaste etc index ~')

    zerowasteList = []
    for idx in zerowaste_df.index :
        if zerowaste_df.iloc[idx , 4] == '기타' or zerowaste_df.iloc[idx , 4] == 0 :
            zerowasteList.append({
                'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
                'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
                'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
                'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
                'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
                'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
                'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
                'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
                'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
                'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() , # numpy
                'WWGScore': (zerowaste_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': zerowaste_df.iloc[idx, :].추천장소,
            })
    print('zerowasteList etc complete!!')

    return JsonResponse(zerowasteList, safe=False)


# vegan data - 완료
# 전체
def vegan_data_all(request) :
    print('mapApp vegan index ~')

    veganList = []
    for idx in vegan_df.index:
        veganList.append({
            'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
            'name': vegan_df.iloc[idx, :].상호명,
            'number': vegan_df.iloc[idx, :].전화번호,
            'address': vegan_df.iloc[idx, :].소재지,
            'category': vegan_df.iloc[idx, :].업종,
            'about': vegan_df.iloc[idx, :].설명,
            'imgURL': vegan_df.iloc[idx, :].imgURl,
            'img': vegan_df.iloc[idx, :].jpg,
            'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
            'lng': (vegan_df.iloc[idx, :].경도).tolist(),  # numpy
            'WWGScore': (vegan_df.iloc[idx, :].WWGScore).tolist(),  # numpy
            'recomm': vegan_df.iloc[idx, :].추천장소,
        })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)

# 멤버쉽
def vegan_membership(request) :
    print('mapApp vegan index ~')
    vegan_sample_df = vegan_df.sample(n=10)
    vegan_membership_df = vegan_sample_df.reset_index()

    veganList = []
    for idx in vegan_membership_df.index:
        veganList.append({
            'id': (vegan_membership_df.iloc[idx, :].번호).tolist(),  # numpy
            'name': vegan_membership_df.iloc[idx, :].상호명,
            'number': vegan_membership_df.iloc[idx, :].전화번호,
            'address': vegan_membership_df.iloc[idx, :].소재지,
            'category': vegan_membership_df.iloc[idx, :].업종,
            'about': vegan_membership_df.iloc[idx, :].설명,
            'imgURL': vegan_membership_df.iloc[idx, :].imgURl,
            'img': vegan_membership_df.iloc[idx, :].jpg,
            'lat': (vegan_membership_df.iloc[idx, :].위도).tolist(),  # numpy
            'lng': (vegan_membership_df.iloc[idx, :].경도).tolist(),  # numpy
            'WWGScore': (vegan_membership_df.iloc[idx, :].WWGScore).tolist(),  # numpy
            'recomm': vegan_membership_df.iloc[idx, :].추천장소,
        })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)

# 한식
def vegan_data_kor(request) :
    print('mapApp vegan kor index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx , 4] == '한식' :
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist(),  # numpy
                'WWGScore': (vegan_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': vegan_df.iloc[idx, :].추천장소,
            })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)

# 양식
def vegan_data_wes(request) :
    print('mapApp vegan wes index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 4] == '양식':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist(),  # numpy
                'WWGScore': (vegan_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': vegan_df.iloc[idx, :].추천장소,
            })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)

# 중식
def vegan_data_chi(request) :
    print('mapApp vegan chi index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 4] == '중식':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist(),  # numpy
                'WWGScore': (vegan_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': vegan_df.iloc[idx, :].추천장소,
            })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)

# 일식
def vegan_data_jap(request) :
    print('mapApp vegan jap index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 4] == '일식':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist(),  # numpy
                'WWGScore': (vegan_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': vegan_df.iloc[idx, :].추천장소,
            })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)

# 카페
def vegan_data_cafe(request) :
    print('mapApp vegan cafe index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 4] == '카페':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist(),  # numpy
                'WWGScore': (vegan_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': vegan_df.iloc[idx, :].추천장소,
            })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)

# 베이커리
def vegan_data_bake(request) :
    print('mapApp vegan bake index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 4] == '베이커리':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist(),  # numpy
                'WWGScore': (vegan_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': vegan_df.iloc[idx, :].추천장소,
            })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)

# 분식/술집/뷔페식/기타
def vegan_data_etc(request) :
    print('mapApp vegan etc index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 4] == '분식' or vegan_df.iloc[idx , 4] == '술집' or vegan_df.iloc[idx , 4] == '뷔페식' or vegan_df.iloc[idx , 4] == '기타' :
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist(),  # numpy
                'WWGScore': (vegan_df.iloc[idx, :].WWGScore).tolist(),  # numpy
                'recomm': vegan_df.iloc[idx, :].추천장소,
            })
    print('veganList all complete!!')

    return JsonResponse(veganList, safe=False)


# Login page
# 로그인
def login(request) :
    response_data={}
    if request.method == 'POST' :
        login_username=request.POST.get('user_id',None)
        login_password=request.POST.get('user_pwd',None)
        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else :
            myuser = WwgUser.objects.get(user_id=login_username)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            # if check_password(login_password, myuser.user_pwd):
            if (login_password == myuser.user_pwd):
                request.session['user'] = myuser.user_id
                print(request.session['user'],'~~~~~~~~~~~')
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('main')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."
                return render(request, 'map/login.html',response_data)
    return render(request , 'map/login.html')

# 로그아웃
def logout(request) :
    auth.logout(request)
    return HttpResponseRedirect('../main')

#
def join(request):
    return redirect('main')

# 회원가입
def registerForm(request):
    if request.method == 'POST':
        print('RegisterForm index ~ ')
        # 딕셔너리 형태
        print('POST~~~~~')
        print(request.POST.get('user_id', None))
        user_id = request.POST.get('user_id', None)
        user_pwd = request.POST.get('user_pwd', None)
        user_birthyear = request.POST.get('user_birthyear', None)
        res_data = {}
        if not (user_id and user_pwd and user_birthyear):
            res_data['error'] = "모든 값을 입력해야 합니다."
        else:
            user = WwgUser(user_id=user_id, user_pwd=make_password(user_pwd), user_birthyear=user_birthyear)
            user.save()
        return render(request, 'map/about.html', res_data)  # register를 요청받으면 registerForm.html 로 응답.
    return render(request, 'map/registerForm.html')


# csv to model
def CsvToModel(request):
    # [WwgUser]
    path = 'C:/Users/user/PJT/WWG/rootWEB/mapApp/db/WwgUsers.csv'
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print('----', reader)
    z_list = [];
    idx = 0
    for row in reader:
        if idx != 0:
            z_list.append(WwgUser(
                user_id=row[0],
                user_pwd=row[1],
                user_birthyear=row[2],
            ))
        idx += 1
    WwgUser.objects.bulk_create(z_list)

    # [Zerowaste Shop]
    path = 'C:/Users/user/PJT/WWG/rootWEB/mapApp/db/Zerowaste.csv'
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print('----', reader)
    z_list = [];
    idx = 0
    for row in reader:
        if idx != 0:
            z_list.append(WwgZerowaste(
                index=row[0],
                name=row[1],
                number=row[2],
                address=row[3],
                category=row[4],
                about=row[5],
                imgURL=row[6],
                img=row[7],
                lat=float(row[8]),
                lng=float(row[9]),
                rating=float(row[10]),
                review1=row[11],
                review2=row[12],
                WWGScore=float(row[13]),
                Recomm=row[14],
            ))
        idx += 1
    WwgZerowaste.objects.bulk_create(z_list)

    # [Vegan Food Shop]
    path = 'C:/Users/user/PJT/WWG/rootWEB/mapApp/db/Veganfood.csv'
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print('----', reader)
    z_list = [];
    idx = 0
    for row in reader:
        if idx != 0:
            z_list.append(WwgVegan(
                index=row[0],
                name=row[1],
                number=row[2],
                address=row[3],
                category=row[4],
                about=row[5],
                imgURL=row[6],
                img=row[7],
                lat=float(row[8]),
                lng=float(row[9]),
                rating=float(row[10]),
                review1=row[11],
                review2=row[12],
                WWGScore=float(row[13]),
                Recomm=row[14],
            ))
        idx += 1
    WwgVegan.objects.bulk_create(z_list)

    # [TopPlace]
    print('Create TopPlace model')
    path = 'C:/Users/user/PJT/WWG/rootWEB/mapApp/db/TopPlace.csv'
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print('----', reader)
    z_list = [];
    idx = 0
    for row in reader:
        if idx != 0:
            z_list.append(TopPlace(
                TopVegan=row[0],
                TopZerowaste=row[1],
                Date=row[2],
            ))
        idx += 1
    TopPlace.objects.bulk_create(z_list)

    # [WwgUsersRecomm]
    print('Create WwgUsersRecomm model')
    # path = 'C:/Users/user/PJT/WeWantGreen/WWG_FINAL/pythonProject1/rootWEB/db/WwgUsersRecomm.csv'
    path = 'C:/Users/user/PJT/WWG/rootWEB/mapApp/db/WwgUsersRecomm.csv'
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print('----', reader)
    z_list = [];
    idx = 0
    for row in reader:
        if idx != 0:
            z_list.append(WwgUserRecomm(
                user_id=row[0],
                vegan_recomm=row[1],
                zerowaste_recomm=row[2],
            ))
        idx += 1
    WwgUserRecomm.objects.bulk_create(z_list)
    return HttpResponse('create model~~~~~~')


# Board page
def board(request):
    print('mapApp index ~ ')
    return render(request, 'map/board.html')

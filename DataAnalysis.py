import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import mean_squared_error
from datetime import datetime

def get_unseen_movies(ratings_matrix, userId):
    # userId로 입력받은 사용자의 모든 영화 정보를 추출해 Series로 반환
    # 반환된 user_rating은 영화명을 인덱스로 가지는 Series 객체임
    user_rating = ratings_matrix.loc[userId,:]
    
    # user_rating이 0보다 크면 기존에 관람한 영화임. 대상인덱스를 추출해 list 객체로 만듦
    idx = user_rating > 0
    already_seen =user_rating[idx].index.tolist()
    
    # 모든 영화명을 list 객체로 만듦
    movies_list =ratings_matrix.columns.tolist()
    
    #list comprehension으로 already_seen에 해당하는 영화는 movies_list에서 제외함.
    unseen_list = [movie for movie in movies_list if movie not in already_seen]
    
    return unseen_list
def recomm_movie_by_userid(pred_df, userId, unseen_list, top_n=10):
    # 예측 평점 DataFrame에서 사용자 id 인덱스와 unseen_list로 돌아온 영화명 컬럼을 추출하여
    # 가장 예측 평점이 높은 순으로 정렬
    recomm_movies = pred_df.loc[userId,unseen_list].sort_values(ascending=False)[:top_n]
    return recomm_movies

# 실제 행렬과 예측 행렬의 오차를 구하는 함수
def get_rmse(R,P,Q,non_zeros):
    error=0
    
    full_pred_matrix = np.dot(P,Q.T)
    
    #여기서 non_zeros는 아래함수에서 확인 할 수 있다.
    x_non_zero_ind = [non_zeros[0] for non_zeros in non_zeros]
    y_non_zero_ind = [non_zeros[1] for non_zeros in non_zeros]
    
    # 원 행렬 R 에서 0이 아닌 값들만 추출한다.
    R_non_zeros=R[x_non_zero_ind,y_non_zero_ind]
    
    # 예측 행렬에서 원 행렬 R에서 0이 아닌 위치의 값들만 추출하여 저장한다.
    full_pred_matrix_non_zeros = full_pred_matrix[x_non_zero_ind,y_non_zero_ind]
    
    mse =mean_squared_error(R_non_zeros, full_pred_matrix_non_zeros)
    rmse = np.sqrt(mse)
    
    return rmse

def matrix_factorization(R,K, steps=200,learning_rate=0.1, r_lambda=0.01):
    num_users, num_items= R.shape
    # P와 Q 매트릴스의 크기를 지정하고 정규 분포를 가진 랜덤한 값으로 입력
    np.random.seed(1)
    P=np.random.normal(scale=1./K, size=(num_users,K))
    Q=np.random.normal(scale=1./K, size=(num_items,K))
    
    prev_rmse=10000
    break_count=0
    
    # R>0인 행 위치, 열 위치, 값을 non_zeros 리스트에 저장
    non_zeros = [(i,j,R[i,j]) for i in  range(num_users) for j in range(num_items) if R[i,j]>0]
    
    # SGD 기법으로 P와 Q 매트릭스를 계속 업데이트
    for step in range(steps):
        for i, j, r in non_zeros :
            #실제 값과 예측값의 차이인 오류 값 구함
            eij = r - np.dot(P[i,:], Q[j,:].T)
            # Regularization을 반영한 SGD 업데이트 공식적용
            P[i,:]=P[i,:]+learning_rate*(eij*Q[j,:]-r_lambda*P[i,:])
            Q[j,:]=Q[j,:]+learning_rate*(eij*P[i,:]-r_lambda*Q[j,:])
            
        rmse = get_rmse(R,P,Q, non_zeros)
        if step %10 ==0 :
            print('iter step:{0}, rmse : {1:4f}'.format(step,rmse))
            
    return P,Q

def get_mse(pred, actual):
    # 평점이 있는 실제 영화만 추출
    pred = pred[actual.nonzero()].flatten()
    actual = actual[actual.nonzero()].flatten()
    return mean_squared_error(pred,actual)
# print('아이템 기반 모든 최근접 이웃 MSE:', get_mse(clicks_pred, Click_matrix.values))


def predict_rating_topsim(rating_arr, item_sim_arr, n=20) :
    # 사용자-아이템 평점 행렬 크기만큼 0으로 채운 예측행렬 초기화
    pred = np.zeros(rating_arr.shape)
    
    # 사용자-아이템 평점행렬의 열 크기 만큼 확인
    for col in range(rating_arr.shape[1]):
        # 유사도 행열에서 유사도가 큰 순으로 n개 데이터 행렬의 인덱스 반환
        top_n_items = [np.argsort(item_sim_arr[:,col])[:-n-1:-1]]
        # 개인화된 예측 평점을 계산
        for row in range(rating_arr.shape[0]):
            pred[row,col] = item_sim_arr[col,:][top_n_items].dot(rating_arr[row,:][top_n_items].T)
            pred[row,col] /= np.sum(np.abs(item_sim_arr[col,:][top_n_items]))
    return pred

#--------------------------------------------------------------------
# WWG Score계산 하기
#--------------------------------------------------------------------
#loading data
df = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\veganfood_review.csv')
# df = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\zerowaste_review.csv')

# Convert objecttype to floattype 
# 방문자리뷰
df['review1'] = df['review1'].str.replace(',', '').astype('int64')
# 블로그리뷰
df['review2'] = df['review2'].str.replace(',', '').astype('int64')
# 리뷰 
df['review'] = df['review1'] + df['review2']

# 0-1 Scaling ('rating' 'review')
MinMaxScaler = MinMaxScaler()

rating = df['rating'].values.reshape(-1,1) # 2차원으로 변경
MinMaxScaler.fit(rating)
Scaled_rating = pd.DataFrame(MinMaxScaler.fit_transform(pd.DataFrame(rating)),columns=['rating'])
df['Scaled_rating'] = Scaled_rating

review = df['review'].values.reshape(-1,1) # 2차원으로 변경
MinMaxScaler.fit(review)
Scaled_review = pd.DataFrame(MinMaxScaler.fit_transform(pd.DataFrame(review)),columns=['review'])
df['Scaled_review'] = Scaled_review

# WWG_Score 5점 만점 (평점 가중치 : 3 / 리뷰수 가중치 : 2)
df['WWGScore'] = 3*df['Scaled_rating'] + 2*df['Scaled_review']
df[['WWGScore','Scaled_rating','Scaled_review']].head()

df.to_csv('./veganfood_WWGScore.csv',index=False) 
# df.to_csv('./zerowaste_WWGScore.csv',index=False) 

#--------------------------------------------------------------------
# 추천 알고리즘
# 1. 사용자의 행동 예측 (Matrix Facotrization)
# 2. 장소간 유사도 (Cosine Smilarity) 
#    사용되는 요소 : 사용자 행동 / 거리 / 업종 / WWGScore
#--------------------------------------------------------------------
WwgUsers = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\WwgUsers.csv')
Click = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\ZerowasteClick.csv')
# VeganMat = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\veganfood_WWGScore.csv')
VeganMat = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\zerowaste_WWGScore.csv')
# Vegan_df = VeganMat[['번호', '상호명','소재지', '업종', '설명(판매메뉴)','WWGScore']]
Vegan_df = VeganMat[['번호', '상호명','소재지', '업종', '설명','WWGScore']]
WWGScore = Vegan_df['WWGScore']

# User x Place 형태로 DF 생성
Click_matrix = Click.pivot_table('cnt',index='user_id', columns='name_index')
Click_matrix = Click_matrix.fillna(0) # NaN 값을 0으로 변환

# [1. 사용자의 행동 예측 (Matrix Facotrization)]
# steps = SGD 횟수 / K= 잠재요인 차원 수 / 학습률과 L2 Regularization 계수는 모두 0.01으로 설정
P,Q = matrix_factorization(Click_matrix.values, K=50, steps=200, learning_rate=0.01,r_lambda=0.01)
pred_matrix = np.dot(P,Q.T)

clicks_pred_matrix = pd.DataFrame(data=pred_matrix, index=Click_matrix.index, columns=Click_matrix.columns)
# clicks_pred_matrix.to_csv('./VeganClick_pred.csv',index=False)
clicks_pred_matrix.to_csv('./ZerowasteClick_pred.csv',index=False)

# [2. 장소간 유사도 (Cosine Smilarity)]
#--- 1. 사용자 행동 유사도
Click_matrix_T = clicks_pred_matrix.transpose()
item_sim = cosine_similarity(Click_matrix_T,Click_matrix_T)

#--- 2. 거리 유사도
count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
dist_category = count_vect_category.fit_transform(Vegan_df['소재지']) 
dist_simi_cate = cosine_similarity(dist_category, dist_category) 
dist_simi_cate_sorted_ind = dist_simi_cate.argsort()[:, ::-1]

#--- 3. 카테고리 유사도
count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
place_category = count_vect_category.fit_transform(Vegan_df['업종']) 
place_simi_cate = cosine_similarity(place_category, place_category) 
place_simi_cate_sorted_ind = place_simi_cate.argsort()[:, ::-1]

# 공식 병합하기 
place_simi_co = (+ item_sim*0.1 # 공식 1. 사용자 행동
                + dist_simi_cate*0.4 # 공식 2. 거리
                + place_simi_cate*0.4 # 공식 3. 카테고리 
                + np.repeat([WWGScore], len(WWGScore) , axis=0)*0.1  # 공식 . 평점&리뷰
                )

#--------------------------------------------------------------------
# 사용자별 추천 장소 Top6 뽑기
#--------------------------------------------------------------------
WwgUsers = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\WwgUsers.csv')
recomm_List=[]
for UserName in np.unique(WwgUsers.user_id) :
# 사용자가 관람하지 않은 영화명 추출
    unseen_list = get_unseen_movies(Click_matrix,UserName)
    # 잠재 요인 협업 필터링으로 영화 추천
    recomm_place = recomm_movie_by_userid(clicks_pred_matrix, UserName, unseen_list, top_n=6)
    recomm_dict = {}
    tmp_place= list(recomm_place.index)
    tmp_predscore = list(recomm_place.values)
    for place, predscore in zip(tmp_place,tmp_predscore):
        recomm_dict[place]=predscore
    recomm_List.append(recomm_dict)

# WwgUsers.vegan_recomm = recomm_List
WwgUsers.zerowaste_recomm = recomm_List
WwgUsers.to_csv('./WwgUsers.csv',index=False) 

#--------------------------------------------------------------------
# 각 상호에 대해 추천장소 추출
#--------------------------------------------------------------------
# 큰 값 부터 순서대로 데이터의 index를 반환해줌
item_sim_sorted_ind = item_sim.argsort()[:, ::-1] 

# place recommend algorithm
def find_simi_place(df, sorted_ind, place_name, top_n=10):
    place_title = df[df['상호명'] == place_name]
    place_index = place_title.index.values
    similar_indexes = sorted_ind[place_index, :(top_n)]
    # return 1 dimension array 
    similar_indexes = similar_indexes.reshape(-1)
    return df.iloc[similar_indexes]

# 각 상호에 대해 추천장소 추출
rec_list = []
for place in Vegan_df['상호명'] :
    rec_label = find_simi_place(Vegan_df, item_sim_sorted_ind, place, 5)['상호명']
    cn=0; rec = ''
    for label in rec_label :
        if cn==0 :
            rec = label
        else :
            rec = rec +' / '+label
        cn+=1
    rec_list.append(rec)
    
Vegan_df['추천장소'] =rec_list
# Vegan_df.to_csv('./veganfood_Recomm.csv',index=False) 
Vegan_df.to_csv('./Zerowaste_Recomm.csv',index=False) 


#--------------------------------------------------------------------
# 인기장소 Top6 뽑기 
#--------------------------------------------------------------------

TopPlace = pd.read_csv('C:/Users/user/PJT/WeWantGreen/rootWEB/db/TopPlace.csv')
# [Vegan]
Mat = pd.read_csv('C:/Users/user/PJT/WeWantGreen/rootWEB/db/Zerowaste.csv')
WWGScore = Mat['WWGScore'] #'번호', '상호명','소재지', '업종', '설명(판매메뉴)',

clicks_pred_matrix = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\VeganClick_pred.csv')
ClickScore = clicks_pred_matrix.apply(sum,axis=0)
ClickScore= ClickScore.reset_index(drop=True)
Score = WWGScore + (ClickScore * 0.1)

TopVegan=[]; top_dict = {}
Score = Score.sort_values(ascending=False)[:3]
tmp_place= list(Score.index)
tmp_score = list(Score.values)
for place, score in zip(tmp_place,tmp_score):
    top_dict[place]=score

TopVegan.append(top_dict)

# [Zerowaste]
Mat = pd.read_csv('C:/Users/user/PJT/WeWantGreen/rootWEB/db/Veganfood.csv')
WWGScore = Mat['WWGScore'] #'번호', '상호명','소재지', '업종', '설명(판매메뉴)',

clicks_pred_matrix = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\ZerowasteClick_pred.csv')
ClickScore = clicks_pred_matrix.apply(sum,axis=0)
ClickScore= ClickScore.reset_index(drop=True)
Score = WWGScore + (ClickScore * 0.1)

TopZerowaste=[]; top_dict = {}
Score = Score.sort_values(ascending=False)[:3]
tmp_place= list(Score.index)
tmp_score = list(Score.values)
for place, score in zip(tmp_place,tmp_score):
    top_dict[place]=score

TopZerowaste.append(top_dict)
# [Date]
Date = datetime.today().strftime("%Y-%m-%d")

TopPlace.loc[len(TopPlace)] = [TopVegan, TopZerowaste, Date]
TopPlace.to_csv('C:/Users/user/PJT/WeWantGreen/rootWEB/db/TopPlace.csv',index=False)


# from ast import literal_eval
# TopPlace = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\TopPlace.csv')
# TopPlace['TopVegan'] = TopPlace['TopVegan'].apply(literal_eval)
# TopPlace['TopVegan'].apply(lambda x: [y.keys() for y in x])
# TopPlace['TopVegan'].apply(lambda x: [y.values() for y in x])
# literal_eval(TopPlace['TopVegan'][0])[0].keys()

# #--------------------------------------------------------------------
# 이미지 리사이징
# #--------------------------------------------------------------------
from PIL import Image
import os

file_list = os.listdir('C:/Users/user/PJT/WeWantGreen/rootWEB/mapApp/static/resources/theme/images/zerowaste/')

for jpg in file_list :
    path = 'C:/Users/user/PJT/WeWantGreen/rootWEB/mapApp/static/resources/theme/images/zerowaste/'+jpg
    img = Image.open(path)
    img_resize = img.resize((460, 410))
    img_resize = img_resize.convert('RGB')
    img_resize.save(path)

file_list = os.listdir('C:/Users/user/PJT/WeWantGreen/rootWEB/mapApp/static/resources/theme/images/vegan/')

for jpg in file_list :
    path = 'C:/Users/user/PJT/WeWantGreen/rootWEB/mapApp/static/resources/theme/images/vegan/'+jpg
    img = Image.open(path)
    img_resize = img.resize((460, 410))
    img_resize = img_resize.convert('RGB')
    img_resize.save(path)

# #--------------------------------------------------------------------
# # USER별 오늘의 PICK (Click Matrix 이용)
# # 1. 사용자의 행동 예측 (MSE)
# #--------------------------------------------------------------------
# Click = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\VeganClick.csv')
# VeganMat = pd.read_csv('C:\\Users\\user\\PJT\\WeWantGreen\\veganfood_WWGScore.csv')
# Vegan_df = VeganMat[['번호', '상호명','소재지', '업종', '설명(판매메뉴)','WWGScore']]
# WWGScore = Vegan_df['WWGScore']

# # User x Place 형태로 DF 생성
# Click_matrix = Click.pivot_table('cnt',index='user_id', columns='name_index')
# Click_matrix = Click_matrix.fillna(0) # NaN 값을 0으로 변환

# # 장소간 유사도 산출 (행을 기준으로 유사도가 측정됨)
# Click_matrix_T = Click_matrix.transpose()

# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer

# #--- 1. 거리 유사도
# count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
# dist_category = count_vect_category.fit_transform(Vegan_df['소재지']) 
# dist_simi_cate = cosine_similarity(dist_category, dist_category) 
# dist_simi_cate_sorted_ind = dist_simi_cate.argsort()[:, ::-1]

# #--- 2. 카테고리 유사도
# count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
# place_category = count_vect_category.fit_transform(Vegan_df['업종']) 
# place_simi_cate = cosine_similarity(place_category, place_category) 
# place_simi_cate_sorted_ind = place_simi_cate.argsort()[:, ::-1]

# # 공식 병합하기 
# place_simi_co = (
#                  + dist_simi_cate * 0.4 # 공식 1. 거리 유사도
#                  + place_simi_cate * 0.4 # 공식 2. 카테고리 유사도
#                  + np.repeat([WWGScore], len(WWGScore) , axis=0) * 0.25  # 공식 3. WWGScore
#                 #  + np.repeat([ClickScore], len(ClickScore) , axis=0) * 0.05  # 공식 4. ClickScore 관심의 정도
#                 )

# item_sim = cosine_similarity(Click_matrix_T,Click_matrix_T)
# item_sim = 0.05*(item_sim) + place_simi_co
# item_sim_df = pd.DataFrame(item_sim,index=Click_matrix.columns, columns=Click_matrix.columns)
# item_sim_df.head()

# # 개인별 행동을 예측해보자.
# # 특정 장소에 대해 Click수가 없을 경우, NaN으로 할당.
# def predict_click(ratings_arr, item_sim_arr) :
#     ratings_pred = ratings_arr.dot(item_sim_arr) / np.array([np.abs(item_sim_arr).sum(axis=1)])
#     return ratings_pred

# # 예측한 클릭수에 대한 성능 평가 MSE를 구함
# from sklearn.metrics import mean_squared_error

# def get_mse(pred, actual):
#     # 평점이 있는 실제 영화만 추출
#     pred = pred[actual.nonzero()].flatten()
#     actual = actual[actual.nonzero()].flatten()
#     return mean_squared_error(pred,actual)
# # print('아이템 기반 모든 최근접 이웃 MSE:', get_mse(clicks_pred, Click_matrix.values))


# def predict_rating_topsim(rating_arr, item_sim_arr, n=20) :
#     # 사용자-아이템 평점 행렬 크기만큼 0으로 채운 예측행렬 초기화
#     pred = np.zeros(rating_arr.shape)
    
#     # 사용자-아이템 평점행렬의 열 크기 만큼 확인
#     for col in range(rating_arr.shape[1]):
#         # 유사도 행열에서 유사도가 큰 순으로 n개 데이터 행렬의 인덱스 반환
#         top_n_items = [np.argsort(item_sim_arr[:,col])[:-n-1:-1]]
#         # 개인화된 예측 평점을 계산
#         for row in range(rating_arr.shape[0]):
#             pred[row,col] = item_sim_arr[col,:][top_n_items].dot(rating_arr[row,:][top_n_items].T)
#             pred[row,col] /= np.sum(np.abs(item_sim_arr[col,:][top_n_items]))
#     return pred

# clicks_pred = predict_rating_topsim(Click_matrix.values, item_sim_df.values, n=20)
# print('아이템기반 최근점 TOP-20 이웃 MSE:', get_mse(clicks_pred, Click_matrix.values))

# # 계산된 예측 평점 데이터는 DataFrame으로 재생성
# clicks_pred_matrix = pd.DataFrame(data=clicks_pred, index=Click_matrix.index, columns = Click_matrix.columns)
# # clicks_pred_matrix.head(3)

# # 사용자별 추천 장소 Top3 뽑기
# user_rating_id = Click_matrix.loc['User1',:]
# user_rating_id[user_rating_id>0].sort_values(ascending=False)[:3]

# # 인기장소 Top6 뽑기 (WWGScore = 평점*3 / 리뷰수*2 / 예측된 클릭수*0.05)
# clicks_pred_matrix = clicks_pred_matrix.fillna(0)
# ClickScore = clicks_pred_matrix.apply(sum,axis=0)
# WWGScore = WWGScore + ClickScore * 0.05
# WWGScore.sort_values(ascending=False)[:6]
# #[참고] unseen data에 대한 추천리스트도 뽑을 수 있음

# # 각 상호에 대해 추천장소 추출
# # 큰 값 부터 순서대로 데이터의 index를 반환해줌
# item_sim_sorted_ind = item_sim.argsort()[:, ::-1] 

# # place recommend algorithm
# def find_simi_place(df, sorted_ind, place_name, top_n=10):
#     place_title = df[df['상호명'] == place_name]
#     place_index = place_title.index.values
#     similar_indexes = sorted_ind[place_index, :(top_n)]
#     # return 1 dimension array 
#     similar_indexes = similar_indexes.reshape(-1)
#     return df.iloc[similar_indexes]

# # 각 상호에 대해 추천장소 추출
# rec_list = []
# for place in Vegan_df['상호명'] :
#     rec_label = find_simi_place(Vegan_df, item_sim_sorted_ind, place, 5)['상호명']
#     cn=0; rec = ''
#     for label in rec_label :
#         if cn==0 :
#             rec = label
#         else :
#             rec = rec +' / '+label
#         cn+=1
#     rec_list.append(rec)
    
# Vegan_df['추천장소'] =rec_list
# Vegan_df.to_csv('./veganfood_Recommandation.csv',index=False) 

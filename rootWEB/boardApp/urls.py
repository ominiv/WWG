from django.contrib import admin
from django.urls import path
from mapApp import views
from django.urls import path
from boardApp import views  # 해당 앱의 뷰를 불러온다.
from django.core.paginator import Paginator
from django.conf.urls.static import static
from django.conf import settings

app_name = 'boardApp'  # 이름공간을 지정.

urlpatterns = [
    path('', views.list, name='list'),  # list를 보여주는 뷰와 연결한다.
    path('list2', views.list2, name='list2') , #자유게시판
    path('post/', views.post, name='post'), #글의 작성화면
    path('post/<int:pk>', views.detail, name='detail') , #게시글
    path('post2/', views.post2, name='post2') ,
    path('post2/<int:pk>/', views.detail2, name='detail2') , #게시글
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
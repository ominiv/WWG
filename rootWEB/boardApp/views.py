from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def list(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    boards = Board.objects.order_by('-created_date')  # created_date를 역순으로 정렬
    # 페이징처리
    paginator = Paginator(boards, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'boards': page_obj}

    return render(request , 'board/list.html', context)




def list2(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    boards2 = Board2.objects.order_by('-created_date')  # created_date를 역순으로 정렬
    # 페이징처리
    paginator = Paginator(boards2, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'boards2': page_obj}
    return render(request , 'board/list2.html', context)


#게시글 페이지
def detail(request,pk):
    boards = get_object_or_404(Board, id=pk)
    context = {
        'boards': boards,
    }
    boards.hits += 1
    boards.save()
    return render(request, 'board/detail.html', context)

#게시글 페이지
def detail2(request,pk):
    boards2 = get_object_or_404(Board2, id=pk)
    context2 = {
        'boards2': boards2,
    }
    boards2.hits += 1
    boards2.save()
    return render(request, 'board/detail2.html', context2)

#글쓰기 페이지
def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        if 'mainphoto' in request.FILES:
            mainphoto = request.FILES['mainphoto']
        else:
            mainphoto = False
        board = Board(author=author, title=title, content=content, mainphoto=mainphoto)
        board.save()
        return HttpResponseRedirect('/board/')
    else:
        return render(request, 'board/post.html')

#글쓰기 페이지2
def post2(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        if 'mainphoto' in request.FILES:
            mainphoto = request.FILES['mainphoto']
        else:
            mainphoto = False
        board2 = Board2(author=author, title=title, content=content, mainphoto=mainphoto)
        board2.save()
        return HttpResponseRedirect('/board/list2')
    else:
        return render(request, 'board/post2.html')
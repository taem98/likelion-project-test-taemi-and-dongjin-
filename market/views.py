from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Book, Room, ProductComment, BookComment, RoomComment, Comment
from .forms import ProductForm, BookForm, RoomForm, ProductCommentForm, BookCommentForm, RoomCommentForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# def list(request, name):
def list(request):
    product_all = Product.objects.all()
    book_all = Book.objects.all()
    room_all = Room.objects.all()
    return render(request, 'market/list.html', {'products' : product_all, 'books':book_all, 'rooms':room_all,})

    # if name == 'book':
    #     return render(request, 'list.html',{
    #         'books': book_all,
    #         }
    #     )
    # elif name == "product":
    #     return render(request, 'list.html', {
    #         'product': product_all,
    #     })
    # elif name == "room":
    #     return render(request, 'list.html', {
    #         'room': room-all,
    #     })

#product=====================================================================================

def product_hit(request, post_id):
    product = get_object_or_404(Product, id=post_id)
    product.update_counter()
    return redirect('product_detail', post_id = product.pk)


def product_detail(request, post_id):
    product_detail = get_object_or_404(Product, id=post_id)
    form = ProductCommentForm()
    return render(request, 'market/product_detail.html', {'product': product_detail, 'form':form,})


def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', post_id=product.pk)
    else:
        form = ProductForm()
    return render(request, 'market/product_new.html', {'form': form}) 

    

def product_edit(request, post_id):
    product = get_object_or_404(Product, pk = post_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', post_id=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'market/product_new.html', {'form': form})    


def product_delete(request, post_id):
    product = get_object_or_404(Product, id=post_id)
    product.delete()
    return redirect('list')

def product_application(request, post_id):
    product = get_object_or_404(Product, id=post_id)
    # 작성 폼 추가 필요
    return render(request, 'market/product_application.html',)

    
@csrf_exempt
def product_add_comment(request, post_id):
    product = get_object_or_404(Product, id=post_id)
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product.id)
    # book = get_object_or_404(Book, pk=post_id)
    # if request.method == 'POST':
    #     if request.is_ajax(): #ajax쓸떄
    #         form = BookCommentForm(request.POST or None)
    #         data = request.POST.get("commentBody")
    #         if form.is_valid():
    #             comment = form.save(commit=False)
    #             comment.book = book
    #             comment.save()
    #             comments = book.bookcomment_set.all()
    #             a = list(comments.values())
    #             print(a)

    #             # data = {
    #             #     'comments':comments.values(),
    #             # }

    #             # ajax가 아닐 때
    #             # return redirect('detail', post.id)
    #             # ajax를 사용할 때
    #             return JsonResponse(a, safe=False)
    #             # return HttpResponse(json.dumps(comments),content_type='application/json')
    #             # return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    # else:
    #     form = BookCommentForm()
    # return render(request, 'market/book_detail.html', {
    #     'book': book,
    #     'form': form,
    #     }
    # )

@csrf_exempt
def product_add_recomment(request, comment_id):
    comment = get_object_or_404(ProductComment, id = comment_id)
    product = comment.product
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            recomment = form.save(commit=False)
            recomment.product = product
            recomment.recomment = comment
            recomment.save()
            return redirect('product_detail', product.id)


#book=====================================================================================
def book_hit(request, post_id):
    book = get_object_or_404(Book, id=post_id)
    book.update_counter()
    return redirect('book_detail', post_id = book.pk)


def book_detail(request, post_id):
    book_detail = get_object_or_404(Book, id=post_id)
    form = BookCommentForm()
    return render(request, 'market/book_detail.html', {'book':book_detail, 'form':form,})


def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', post_id=book.pk)
    else:
        form = BookForm()
    return render(request, 'market/book_new.html', {'form': form}) 



def book_edit(request, post_id):
    book = get_object_or_404(Book, pk = post_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', post_id=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'market/book_new.html', {'form': form}) 


def book_delete(request, post_id):
    book = get_object_or_404(Book, id=post_id)
    book.delete()
    return redirect('list')

@csrf_exempt
def book_add_comment(request, post_id):
    book = get_object_or_404(Book, id=post_id)
    if request.method == 'POST':
        form = BookCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('book_detail',book.id)
    # book = get_object_or_404(Book, pk=post_id)
    # if request.method == 'POST':
    #     if request.is_ajax(): #ajax쓸떄
    #         form = BookCommentForm(request.POST or None)
    #         data = request.POST.get("commentBody")
    #         if form.is_valid():
    #             comment = form.save(commit=False)
    #             comment.book = book
    #             comment.save()
    #             comments = book.bookcomment_set.all()
    #             a = list(comments.values())
    #             print(a)

    #             # data = {
    #             #     'comments':comments.values(),
    #             # }

    #             # ajax가 아닐 때
    #             # return redirect('detail', post.id)
    #             # ajax를 사용할 때
    #             return JsonResponse(a, safe=False)
    #             # return HttpResponse(json.dumps(comments),content_type='application/json')
    #             # return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    # else:
    #     form = BookCommentForm()
    # return render(request, 'market/book_detail.html', {
    #     'book': book,
    #     'form': form,
    #     }
    # )
    
@csrf_exempt
def book_add_recomment(request, comment_id):
    comment = get_object_or_404(BookComment, id = comment_id)
    book = comment.book
    if request.method == 'POST':
        form = BookCommentForm(request.POST)
        if form.is_valid():
            recomment = form.save(commit=False)
            recomment.book = book
            recomment.recomment = comment
            recomment.save()
            return redirect('book_detail', book.id)

#Room=====================================================================================
def room_hit(request, post_id):
    room = get_object_or_404(Room, id=post_id)
    room.update_counter()
    return redirect('room_detail', post_id = room.pk)


def room_detail(request, post_id):
    room_detail = get_object_or_404(Room, id=post_id)
    form = RoomCommentForm()
    return render(request, 'market/room_detail.html', {'room':room_detail, 'form':form,})


def room_new(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('room_detail', post_id=room.pk)
    else:
        form = RoomForm()
    return render(request, 'market/room_new.html', {'form': form}) 



def room_edit(request, post_id):
    room = get_object_or_404(Room, pk = post_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('room_detail', post_id=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'market/room_new.html', {'form': form}) 


def room_delete(request, post_id):
    room = get_object_or_404(Room, id=post_id)
    room.delete()
    return redirect('list')

    

@csrf_exempt
def room_add_comment(request, post_id):
    room = get_object_or_404(Room, id=post_id)
    if request.method == 'POST':
        form = RoomCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.room = room
            comment.save()
            return redirect('room_detail',room.id)
    # book = get_object_or_404(Book, pk=post_id)
    # if request.method == 'POST':
    #     if request.is_ajax(): #ajax쓸떄
    #         form = BookCommentForm(request.POST or None)
    #         data = request.POST.get("commentBody")
    #         if form.is_valid():
    #             comment = form.save(commit=False)
    #             comment.book = book
    #             comment.save()
    #             comments = book.bookcomment_set.all()
    #             a = list(comments.values())
    #             print(a)

    #             # data = {
    #             #     'comments':comments.values(),
    #             # }

    #             # ajax가 아닐 때
    #             # return redirect('detail', post.id)
    #             # ajax를 사용할 때
    #             return JsonResponse(a, safe=False)
    #             # return HttpResponse(json.dumps(comments),content_type='application/json')
    #             # return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    # else:
    #     form = BookCommentForm()
    # return render(request, 'market/book_detail.html', {
    #     'book': book,
    #     'form': form,
    #     }
    # )
    
@csrf_exempt
def room_add_recomment(request, comment_id):
    comment = get_object_or_404(RoomComment, id = comment_id)
    room = comment.room
    if request.method == 'POST':
        form = RoomCommentForm(request.POST)
        if form.is_valid():
            recomment = form.save(commit=False)
            recomment.room = room
            recomment.recomment = comment
            recomment.save()
            return redirect('room_detail', room.id)

#image_upload=====================================================================================

class ImageUploadView():
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'market/product_new.html',{'photos':photos_list})

    def post(self, request):
        form = ProductImageForm(self.request.POST, self.request.FILES) #FILES로 써도 괜찮은지 알아보기
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': Ture, 'url': product.image.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
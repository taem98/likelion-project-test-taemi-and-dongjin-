from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Book, Room
from .forms import ProductForm, BookForm, RoomForm


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
    return render(request, 'market/product_detail.html', {'product':product_detail})


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
    


#book=====================================================================================
def book_hit(request, post_id):
    book = get_object_or_404(Book, id=post_id)
    book.update_counter()
    return redirect('book_detail', post_id = book.pk)


def book_detail(request, post_id):
    book_detail = get_object_or_404(Book, id=post_id)
    return render(request, 'market/book_detail.html', {'book':book_detail})


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


#Room=====================================================================================
def room_hit(request, post_id):
    room = get_object_or_404(Room, id=post_id)
    room.update_counter()
    return redirect('room_detail', post_id = room.pk)


def room_detail(request, post_id):
    room_detail = get_object_or_404(Room, id=post_id)
    return render(request, 'market/room_detail.html', {'room':room_detail})


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


#image_upload=====================================================================================

class ImageUploadView():
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'market/product_new.html',{'photos':photos_list})

    def post(self, request):
        form = ProductImageForm(self.request.POST, self.request.FILES) #FILES로 써도 괜찮은지 알아보기
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': Ture}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
from django import forms
from .models import Product, Book, Room, ProductComment, BookComment, RoomComment, ProductImages, BookImages, RoomImages

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('price', 'image', 'title', 'text', 'status_content', 'number', 'soldout')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('price', 'image', 'title', 'text', 'status_content', 'number', 'soldout', 'edition')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('price', 'image', 'title', 'text', 'status_content', 'number', 'soldout', 'position')

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('text',)

class BookCommentForm(forms.ModelForm):
    class Meta:
        model = BookComment
        fields = ('text',)

class RoomCommentForm(forms.ModelForm):
    class Meta:
        model = RoomComment
        fields = ('text',)

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(label='Product_Image')    
    class Meta:
        model = ProductImages
        fields = ('image', )

class BookImageForm(forms.ModelForm):
    image = forms.ImageField(label='Book_Image')    
    class Meta:
        model = BookImages
        fields = ('image', )

class RoomImageForm(forms.ModelForm):
    image = forms.ImageField(label='Room_Image')    
    class Meta:
        model = RoomImages
        fields = ('image', )
from django import forms
from .models import Product, Book, Room, ProductComment, BookComment, RoomComment, ProductImages, BookImages, RoomImages


class ProductForm(forms.ModelForm):
    # image = forms.ImageField(label='Product_Image')
    class Meta:
        model = Product
        fields = ('price', 'image', 'title', 'text', 'status_content', 'number', 'soldout',)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('price', 'image', 'title', 'text', 'status_content', 'number', 'soldout', 'edition')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('price', 'image', 'title', 'text', 'status_content', 'number', 'soldout', 'position')

class ProductCommentForm(forms.ModelForm):
    text = forms.CharField(max_length=240, 
        widget=forms.TextInput(attrs={
            'id': 'commentBody',
        }))
    class Meta:
        model = ProductComment
        fields = ('text',)

class BookCommentForm(forms.ModelForm):
    text = forms.CharField(max_length=240, 
        widget=forms.TextInput(attrs={
            'id': 'commentBody',
        }))
    class Meta:
        model = BookComment
        fields = ('text',)

class RoomCommentForm(forms.ModelForm):
    text = forms.CharField(max_length=240, 
        widget=forms.TextInput(attrs={
            'id': 'commentBody',
        }))
    class Meta:
        model = RoomComment
        fields = ('text',)

class ProductImageForm(forms.ModelForm):
    images = forms.ImageField(label='Product_Image')    
    class Meta:
        model = ProductImages
        fields = ('images', )

class BookImageForm(forms.ModelForm):
    images = forms.ImageField(label='Book_Image')    
    class Meta:
        model = BookImages
        fields = ('images', )

class RoomImageForm(forms.ModelForm):
    images = forms.ImageField(label='Room_Image')    
    class Meta:
        model = RoomImages
        fields = ('images', )

class SearchForm(forms.Form):
    CHOICES= (
    ('1', 'book'),
    ('2', 'product'),
    ('3', 'room'),
    )
    select = forms.CharField(widget=forms.Select(choices=CHOICES))
    search = forms.CharField(max_length=200)
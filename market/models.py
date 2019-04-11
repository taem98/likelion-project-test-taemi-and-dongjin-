from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Base(models.Model):
    price = models.IntegerField()                       #가격
    image = models.FileField(upload_to='images/', null=True)                          #메인이미지
    title = models.CharField(max_length=100)            #제목
    text = models.TextField()                           #내용
    status_content = models.CharField(max_length=100)   #물건상태
    number = models.CharField(max_length=20)            #번호
    soldout = models.BooleanField(default=False)        #판매여부

def get_image_filename(instance, filename, model):
    title = instance.model.title
    id = instance.model.id
    slug = slugify(title)
    return "%s_images/%s-%s" % (model, slug, filename)  

class Images(models.Model):
    pass
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image') 

class Comment(models.Model):
    recomment = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=100)

class Product(Base):
    product_hit = models.PositiveIntegerField(default=0)

    def update_counter(self):
        self.product_hit = self.product_hit + 1
        self.save()

class Book(Base):
    edition = models.CharField(max_length=5)
    author = models.CharField(max_length=10)

class Room(Base):
    position = models.CharField(max_length=100)

class ProductComment(Comment):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)

class BookComment(Comment):
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)

class RoomComment(Comment):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE)

class ProductImages(Images):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)

class BookImages(Images):
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)

class RoomImages(Images):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE)



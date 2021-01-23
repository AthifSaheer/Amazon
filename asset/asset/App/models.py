from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    heading = models.CharField(max_length=200)
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.heading

class Goods(models.Model):
    heading = models.CharField(max_length=200)
    url = models.SlugField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products_img')
    wholesale_rate = models.PositiveIntegerField()
    amazon_rate = models.PositiveIntegerField()
    more_about = models.TextField()
    guaranty = models.CharField(max_length=200, null=True, blank=True)
    recover = models.CharField(max_length=200, null=True, blank=True)
    vision_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.heading


class Bucket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    sum_of_amount = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)


class BucketItems(models.Model):
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Bucket: " + str(self.bucket.id) + ", CartProduct: " + str(self.id)

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On The Way", "On The Way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled")
)
METHOD = (
    ("Cash On Delivery ", "Cash On Delivery "),
)
class Order(models.Model):
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    mail_id = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=METHOD)
    payment_completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)


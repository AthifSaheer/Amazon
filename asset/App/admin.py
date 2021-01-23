from django.contrib import admin
from .models import *

admin.site.register([Client, Goods, Group, Bucket, BucketItems, Order])
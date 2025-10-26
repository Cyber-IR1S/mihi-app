from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post  # 1. さっき作ったPostモデルをインポート

# 2. Postモデルを管理画面に登録する
admin.site.register(Post)

#superuserのユーザーネーム:IR1S,password:rem0-rem0
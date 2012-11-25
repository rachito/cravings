from django.contrib import admin
from restaurant.models import Restaurant, Tag, FoodCategory, Branch

admin.site.register(Tag)
admin.site.register(FoodCategory)
admin.site.register(Restaurant)
admin.site.register(Branch)

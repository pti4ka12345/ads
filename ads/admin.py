from django.contrib import admin

from users.models import Location, User
from ads.models import Category, Ad

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Location)
admin.site.register(User)
from django.contrib import admin
from .models import Plans,Promotions,User,CustomerGoals,Brands
# Register your models here.
admin.site.register(Brands)
admin.site.register(Plans)
admin.site.register(Promotions)
admin.site.register(User)
admin.site.register(CustomerGoals)

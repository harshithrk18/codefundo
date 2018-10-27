from django.contrib import admin
from .models import Ngo
from .models import ReliefCamp
from .models import UserProfileInfo, User
# Register your models here.

admin.site.register(Ngo)
admin.site.register(ReliefCamp)
admin.site.register(UserProfileInfo)


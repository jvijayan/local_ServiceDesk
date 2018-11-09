from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from company_management.models import *
from user_management.models import *

admin.site.register(User, UserAdmin)
admin.site.register(Company)

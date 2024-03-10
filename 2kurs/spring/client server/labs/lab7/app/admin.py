
from django.contrib import admin
from .models import Branch, Worker
# Register your models here.
# 1. setting 2. model 3. makemigretions, 4. migrate
# 5.createsuperuser 6.admin
# -u bold -w bold123 on psql
admin.site.register(Branch)
admin.site.register(Worker)

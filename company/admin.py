from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone_number','subject')
    
admin.site.register(Contact, ContactAdmin)
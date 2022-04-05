from django.contrib import admin
from . import models



@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname', 'lname', 'phone', 'created_at',)
#     list_filter = ('id',)
#     search_fields = ('id',)

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Book


# Register your models here.
#admin.site.register(Book)
admin.site.unregister(Group)

#Changing admin header
admin.site.site_header = 'Library Management'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('email',)    #user will not see this email field
    list_display = ('name','author')    #these fields we can see after clicking on books
    list_filter = ('name', )

from django.contrib import admin
from .models import Book, IssuedBooks
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBooks, IssuedBookAdmin)
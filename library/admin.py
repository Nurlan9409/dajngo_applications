from django.contrib import admin
from .models import Book,Autor,BookingBook,Comment
from import_export.admin import ImportExportModelAdmin



@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('author','text','student')
    list_display_links = ('author','text','student')
    search_fields = ('author__first_name','student__first_name','student__last_name')


@admin.register(BookingBook)
class BookingBookAdmin(ImportExportModelAdmin):
    list_display = ('take_date','rent_price','return_date')
    list_display_links = ('take_date','rent_price','return_date')
    search_fields = ('take_date',)

@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    list_display = ('id','first_name','last_name','birth_date')
    list_display_links= ('id','first_name','last_name','birth_date')
    search_fields = ('first_name','last_name','birth_date')
    ordering = ('first_name','id')


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id','name','description','price','author','count')
    list_display_links = ('id','name','description','price','author','count')
    search_fields =('id','name')
    ordering = ('name',)






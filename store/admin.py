from django.contrib import admin

from .models import Category,Book,Review,Slider,Writer

class AddCategory(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,AddCategory)

class AddWriter(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Writer,AddWriter)

class AddBook(admin.ModelAdmin):
    list_display = ['name','price','stock','created','updated','status']
    list_filter = ['status','created','updated']
    list_editable = ['price','stock','status']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book,AddBook)

class AddSlider(admin.ModelAdmin):
    list_display = ['title','created','updated']

admin.site.register(Slider,AddSlider)
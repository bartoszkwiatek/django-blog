from django.contrib import admin
from .models import Post, Comment


"""klasa PostAdmin dodaje nowe opcje do panelu admina"""


def make_published(modeladmin, request, queryset):
    queryset.update(status='published')
    make_published.short_description = "Mark selected stories as published"


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')     #dodaje ww opcje na liście postów
    list_filter = ('status', 'created', 'publish', 'author')        #dodaje mozliwosc filtrowania
    search_fields = ('title', 'body')                               #dodaje wyszukiwarke
    prepopulated_fields = {'slug': ('title',)}                      #wprowadza domyslny 'slug'
    raw_id_fields = ('author',)                                     #zmienia sposob wyboru autora
    date_hierarchy = 'publish'                                      #dodaje filtrowanie daty postow
    ordering = ['status', 'publish']                                #dodaje domyslne sortowanie
    actions = [make_published]                                      # dodaje funkce make_published do panelu admina

admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)
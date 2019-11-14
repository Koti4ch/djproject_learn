from django.contrib import admin
from eventgen.models import Event, Comment
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug_field', 'create_by', 'created', 'status')
    list_filter = ('status', 'created', 'activated', 'create_by')
    search_fields = ('title', 'eventtext')
    prepopulated_fields = {'slug_field': ('title',)}
    raw_id_fields = ('create_by',)
    date_hierarchy = 'activated'
    ordering = ('status', 'activated')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'text')
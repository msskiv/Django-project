from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

# Register your models here.
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_date', 'comment_text')
    readonly_fields = ('comment_date',)
    extra = 0 #выводить количество полей для новых комментариев равное этому параметру

class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('order_status', 'order_name', 'order_phone', 'order_dt')
    readonly_fields = ('order_dt',)
    inlines = [Comment]  #поле класса Comment



admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
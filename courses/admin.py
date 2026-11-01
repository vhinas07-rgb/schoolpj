from django.contrib import admin
from courses.models import Course, Category, Contact


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'price', 'duration', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'teacher__username')
    date_hierarchy = 'created_at'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    search_fields = ('name', 'email', 'subject')
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date', 'updated_date')
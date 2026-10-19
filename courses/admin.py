from django.contrib import admin
from  courses.models import Course,Category



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'price', 'duration', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title',)
    date_hierarchy = 'created_at'

admin.site.register(Category)

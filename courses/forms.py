from django import forms
from courses.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'teacher', 'duration', 'price', 'status', 'category']

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title.strip():
            raise forms.ValidationError("عنوان نمی‌تواند خالی باشد.")
        return title

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("هزینه نمی‌تواند منفی باشد.")
        return price
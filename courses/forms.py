from django import forms
from courses.models import Course


class CourseForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=255, label='عنوان')
    price = forms.IntegerField(required=True, label='هزینه')

    class Meta:
        model = Course
        fields = ['title', 'teacher', 'duration', 'price', 'status', 'category']



    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if not title:
            raise forms.ValidationError("عنوان نمی‌تواند خالی باشد.")
        return title



    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("هزینه نمی‌تواند منفی باشد.")
        return price
    
    
    
class ContactForm(forms.MdelForm): 
    class Meta:
        model = Course
        fields = ['name', 'email', 'subject', 'message']
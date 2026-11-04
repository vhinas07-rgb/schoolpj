from django import forms
from courses.models import Course,Contact


class CourseForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=255, label='عنوان')
    price = forms.IntegerField(required=True,  min_value=0, label='هزینه')
    class Meta:
        model = Course
        fields = ['title', 'teacher', 'duration', 'price', 'status', 'category']

    def clean_title(self):
        title = self.cleaned_data['title']
        return title

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            return price
        
    def clean(self):
        return self.cleaned_data

class ContactForm(forms.ModelForm): 
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
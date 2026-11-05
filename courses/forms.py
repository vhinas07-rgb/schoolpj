from django import forms
from courses.models import Contact, Course


class CourseForm(forms.ModelForm):

    price = forms.IntegerField(min_value=0, label='هزینه')

    class Meta:
        model = Course
        fields = ['title', 'teacher', 'duration', 'price', 'status', 'category', 'image']

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        return title
class ContactForm(forms.ModelForm): 
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
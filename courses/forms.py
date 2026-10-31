from django import forms
from courses.models import Course

class ContactForm(forms.ModelForm):
    
    
     class Meta:
        model = Course
        fields = '__all__'
        
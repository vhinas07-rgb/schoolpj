from django import forms
<<<<<<< HEAD
from courses.models import Course,Contact


class CourseForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=255, label='عنوان')
    price = forms.IntegerField(required=True,  min_value=0, label='هزینه')
=======
from courses.models import Contact, Course


class CourseForm(forms.ModelForm):

    price = forms.IntegerField(min_value=0, label='هزینه')

>>>>>>> baa5f19 (Add course create, update, delete and form validation,edit form and view)
    class Meta:
        model = Course
        fields = ['title', 'teacher', 'duration', 'price', 'status', 'category', 'image']

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        return title

<<<<<<< HEAD
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


=======
    
    
    
>>>>>>> baa5f19 (Add course create, update, delete and form validation,edit form and view)
class ContactForm(forms.ModelForm): 
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
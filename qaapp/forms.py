
from django import forms
# from djrichtextfield.models import RichTextField
# from djrichtextfield.widgets import RichTextWidget
# from ckeditor.widgets import CKEditorWidget
import textwrap
# from django_ace import AceWidget
from qaapp.models import Question, Answer

# from post.models import Post

class tmpForm(forms.Form):

    #  content = forms.CharField(widget=forms.Textarea, label='', help_text='JSON formatted data here.' )
     content = forms.CharField(widget=forms.Textarea, label='', help_text='Your question here.' )

     class Meta:
          # model = Post
          model = Question
     #    fields = '__all__'
          # fields = ['json']

class AnswerForm(forms.Form):
     content = forms.CharField(widget=forms.Textarea, label='', help_text='Your answer here.' )

     class Meta:
          model = Answer
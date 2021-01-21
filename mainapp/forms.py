from django import forms
from .models import Testimonies


class CommentForm(forms.ModelForm):
    class Meta:
        model = Testimonies
        fields = ['Clients_Name','comment']
        widgets = {
            'Clients_Name':forms.TextInput(
                attrs = {
                      "type":"text", "placeholder":"Name*", "required" : "",'placeholder' : "full name"
                }
            ),
            'comment':forms.Textarea(
                attrs = {
                     "rows":"6" , "placeholder":"Message",'placeholder': " comments"
                }
            )
        }

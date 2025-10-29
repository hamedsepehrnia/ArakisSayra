from django import forms

from core.models import Message


from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '100',
                'name': 'name',
                'required': '',
                'data-msg-required': 'لطفا نام خود را وارد کنید.'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control text-left',
                'dir': 'ltr',
                'maxlength': '100',
                'name': 'email',
                'required': '',
                'data-msg-required': 'لطفا آدرس ایمیل خود را وارد کنید.',
                'data-msg-email': 'لطفا یک آدرس ایمیل معتبر وارد کنید.'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '100',
                'name': 'subject',
                'required': '',
                'data-msg-required': 'لطفا موضوع را وارد کنید.'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '8',
                'maxlength': '5000',
                'name': 'message',
                'required': '',
                'data-msg-required': 'لطفا پیام خود را وارد کنید.'
            }),
        }

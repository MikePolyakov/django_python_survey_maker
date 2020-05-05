from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя')
    # last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='email')
    subject = forms.CharField(label='тема')
    message = forms.CharField(label='Сообщение')

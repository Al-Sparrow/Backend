from django import forms
# from django.core.exceptions import ValidationError
# from .models import User
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.dispatch import receiver


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
        ]

    def clean(self):
        cleaned_data = super().clean()
        authorUser = cleaned_data.get("authorUser")

        # if title[0].islower():
        #     raise ValidationError(
        #         {"Заголовок должен начинаться с заглавной буквы"}
        #     )
        #
        # if title == text:
        #     raise ValidationError(
        #         "Текст не должен быть идентичен названию."
        #     )

        return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)

        return user

    def hello_new_user(request, **kwargs):

        html_content = render_to_string(
            'new_user.html',
            {
                'link': f'{settings.SITE_URL}/news/'
            }
        )
        msg = EmailMultiAlternatives(
            subject='',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=request.user.email,

        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
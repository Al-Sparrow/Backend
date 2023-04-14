from django import forms
# from django.core.exceptions import ValidationError
# from .models import User
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
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
        basic_group = Group.objects.get(name='Reader')
        basic_group.user_set.add(user)
        return user
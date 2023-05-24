from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Author, User, Comment
from django.core.cache import cache


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'categoryType',
            'postCategory',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title[0].islower():
            raise ValidationError(
                {"Заголовок должен начинаться с заглавной буквы"}
            )

        if title == text:
            raise ValidationError(
                "Текст не должен быть идентичен названию."
            )

        return cleaned_data




class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')

        return cleaned_data


# class UserForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#
#
#         ]
#
#     def clean(self):
#         cleaned_data = super().clean()
#         authorUser = cleaned_data.get("authorUser")
#
#         # if title[0].islower():
#         #     raise ValidationError(
#         #         {"Заголовок должен начинаться с заглавной буквы"}
#         #     )
#         #
#         # if title == text:
#         #     raise ValidationError(
#         #         "Текст не должен быть идентичен названию."
#         #     )
#
#         return cleaned_data
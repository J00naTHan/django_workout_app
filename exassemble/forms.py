from django import forms
from .models import Exercise, ExerciseSheet
from django.contrib.auth.models import User


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'creator', 'description']


class SheetForm(forms.ModelForm):
    class Meta:
        model = ExerciseSheet
        fields = ['name', 'creator', 'exercises']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined',
        ]

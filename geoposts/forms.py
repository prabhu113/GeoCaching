from django import forms
from django.contrib.auth.models import User
from django.conf import settings


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise forms.ValidationError("This student is not registered. Make sure you talk to your instructor and finish registration")
        print("username")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Invalid password.Check your password and Try again")
        elif user is None:
            pass
            print("Should not get upto this but this is yet to be implemeneted.")

        else:
            print("in here password")
            return password

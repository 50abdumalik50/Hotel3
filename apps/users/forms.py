# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django import forms
# from django.contrib.auth import get_user_model
#
#
# User = get_user_model()
#
#
# class UserCreateForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password1',
#             'password2',
#         ]





from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserCreationForm(UserCreationForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        }
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }


class UserDetailForm(forms.ModelForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'email', 'first_name', 'last_name']


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'




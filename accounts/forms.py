
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ProfileCreationsForm(UserCreationForm):
    """User creation form for a new abstract user"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class ProfileChangeForm(UserChangeForm):
    """User change form for a new abstract user"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
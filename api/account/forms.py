from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import fields
from django.utils.translation import ugettext_lazy as _

from .models import *


class TestForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('bio','location')
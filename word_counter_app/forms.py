from django import forms
from .models import T1, T2, QC


class T1Form(forms.ModelForm):
    class Meta:
        model = T1
        fields = ['id']


class T2Form(forms.ModelForm):
    class Meta:
        model = T2
        fields = ['id']


class QCForm(forms.ModelForm):
    class Meta:
        model = QC
        fields = ['id']

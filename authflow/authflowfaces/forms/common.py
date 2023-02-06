from django import forms

# Base Form
class CommonForm(forms.Form):
    has_result = forms.BooleanField(required=False)
    action_result = forms.CharField(max_length=255, required=False)
    response = forms.CharField(max_length=255, required=False)
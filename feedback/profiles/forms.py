from django import forms

class ProfileForm(forms.Form):
    # user_image = forms.FileField() # sets up form control for accepting files
    user_image = forms.ImageField()

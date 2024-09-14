from django import forms

class Teacher_Input_Form(forms.Form):
    Teacher_Name = forms.CharField(max_length=255)
    Department = forms.CharField(max_length=255)
    Salary = forms.IntegerField()
    # Password = forms.CharField(widget=forms.PasswordInput())  """For Password Field """
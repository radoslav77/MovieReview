from django import forms
from .models import *


#movie add form
class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('name','director','cast','description','relised_date','image')
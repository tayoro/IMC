from django import forms # importation de la bibliotech "forms"
from imc.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('user','nom','prenom','poids','taille')

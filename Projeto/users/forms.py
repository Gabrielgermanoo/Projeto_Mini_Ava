from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length= 100)
    user_type = forms.ChoiceField(choices=[
        ('student', 'Estudante'), ('professor', 'Professor')],
        label='Tipo de usuário',
        help_text=("Selecione o tipo de usuário que está sendo criado."),
        )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise ValidationError("Este email ({}) já está sendo usado!".format(email))
        else:
            return email


        

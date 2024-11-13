from django import forms
from .models import Participant, Supervisor, University, Section

class ParticipantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'supervisor', 'university', 'faculty', 'theme', 'section']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'supervisor': 'Руководитель',
            'university': 'Университет',
            'faculty': 'Институт или факультет',
            'theme': 'Тема',
            'section': 'Секция',
        }

    section = forms.ModelChoiceField(queryset=Section.objects.all(), label='Секция')
    supervisor = forms.ModelChoiceField(queryset=Supervisor.objects.all(), label='Руководитель', required=False)
    university = forms.ModelChoiceField(queryset=University.objects.all(), label='Университет', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Добавляем класс для всех полей формы

from django.shortcuts import render, redirect
from .models import Participant, Section  # Убедитесь, что Section импортирован
from .forms import ParticipantRegistrationForm


def expo(request):
    return render(request, 'expo/expo.html')

def register_participant(request):
    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participants_by_section')  # Здесь должно быть имя вашего URL
        else:
            print(form.errors)  # Для отладки: вывод ошибок формы в консоль
    else:
        form = ParticipantRegistrationForm()
    return render(request, 'expo/register_participant.html', {'form': form})

def participants_by_section(request):
    sort_by = request.GET.get('sort', 'last_name')  # Получаем параметр сортировки из запроса
    sections = Section.objects.prefetch_related('participant_set').all()  # Используем prefetch_related для оптимизации

    # Сортируем участников по выбранному критерию
    for section in sections:
        section.participants = section.participant_set.order_by(sort_by)  # Сортируем участников внутри секции

    return render(request, 'expo/participants_by_section.html', {'sections': sections, 'sort_by': sort_by})

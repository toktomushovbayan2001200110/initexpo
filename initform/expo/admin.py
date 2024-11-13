from django.contrib import admin
from .models import Supervisor, University, Section, Participant

class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'supervisor', 'university', 'section', 'registered_at')
    list_filter = ('section', 'university', 'supervisor')
    search_fields = ('first_name', 'last_name')

# Регистрируем модели
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Participant, ParticipantAdmin)

from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"


class Supervisor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"


class University(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"


class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)
    faculty = models.CharField(max_length=100, blank=True)
    theme = models.CharField(max_length=200, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)  # Связь с секцией
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.section.name}"  # Отображает имя и секцию

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

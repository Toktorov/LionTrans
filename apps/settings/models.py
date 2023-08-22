from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name="Логотип сайта"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайтов"
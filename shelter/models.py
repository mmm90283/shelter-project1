from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка")
    age = models.CharField(max_length=50, verbose_name="Возраст")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='animals/', verbose_name="Фото")
    is_adopted = models.BooleanField(default=False, verbose_name="Уже дома")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.age}"

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"


class AdoptionRequest(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ваше имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    animal = models.ForeignKey(
        Animal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Питомец"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка от {self.name}"

    class Meta:
        verbose_name = "Заявка на усыновление"
        verbose_name_plural = "Заявки на усыновление"
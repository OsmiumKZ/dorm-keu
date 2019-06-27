from django.db import models


class Parent(models.Model):
    """Родители (мама или папа).

    Описание полей:
    name_f -- имя
    name_l -- фамилия
    patronymic -- отчество
    phone -- телефонный номер
    """
    name_f = models.CharField(max_length=100,
                              verbose_name='Имя')
    name_l = models.CharField(max_length=100,
                              verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, 
                                  blank=True, 
                                  null=True,
                                  verbose_name='Отчество')
    phone = models.CharField(max_length=20,
                             verbose_name='Телефонный номер')
    
    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'
        
    def __str__(self):
        return f"{self.name_l} {str(self.name_f)[0]}.\
                {str(self.patronymic)[0] + '.' if self.patronymic != None else ''} \
                ({self.phone})"


class Account(models.Model):
    """Акаунты.

    Описание полей:
    name_f -- имя
    name_l -- фамилия
    patronymic -- отчество
    group -- группа
    gender_id -- ссылка на человеческий пол
    educational_form -- ID формы обучения
    parent_mother -- ссылка на родителя (мама)
    parent_father -- ссылка на родителя (папа)
    citizenship -- гражданство
    uin -- ИИН или номер паспорта
    address -- адрес проживания
    city -- город
    country -- страна
    phone -- телефонный номер
    email -- электронная почта
    privileges -- льготы
    """
    login = models.CharField(max_length=255,
                             verbose_name='Логин')
    password = models.CharField(max_length=255,
                                verbose_name='Пароль')
    name_f = models.CharField(max_length=100,
                              verbose_name='Имя')
    name_l = models.CharField(max_length=100,
                              verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, 
                                  blank=True, 
                                  null=True,
                                  verbose_name='Отчество')
    group = models.CharField(max_length=10, 
                             verbose_name='Группа')
    gender_id = models.PositiveSmallIntegerField(
        verbose_name='Человеческий пол'
    )
    uin = models.CharField(max_length=100,
                           verbose_name='ИИН или номер паспорта')
    address = models.CharField(max_length=100, 
                               blank=True, 
                               null=True,
                               verbose_name='Адрес')
    city = models.CharField(max_length=100, 
                            blank=True, 
                            null=True,
                            verbose_name='Город')
    country = models.CharField(max_length=100, 
                               blank=True, 
                               null=True,
                               verbose_name='Страна')
    citizenship = models.CharField(max_length=100, 
                                   blank=True, 
                                   null=True,
                                   verbose_name='Гражданство')
    parent_mother = models.ForeignKey(Parent, 
                                      on_delete=models.CASCADE, 
                                      blank=True, 
                                      null=True, 
                                      related_name='parent_mother',
                                      verbose_name='Мама')
    parent_father = models.ForeignKey(Parent, 
                                      on_delete=models.CASCADE, 
                                      blank=True, 
                                      null=True, 
                                      related_name='parent_father',
                                      verbose_name='Папа')
    phone = models.CharField(max_length=20, 
                             blank=True, 
                             null=True,
                             verbose_name='Телефонный номер')
    email = models.EmailField(blank=True, 
                              null=True,
                              verbose_name='Электронная почта')
    educational_form = models.PositiveSmallIntegerField(
        blank=True, 
        null=True,
        verbose_name='Форма обучения'
    )
    privileges = models.CharField(max_length=255, 
                                  blank=True, 
                                  null=True,
                                  verbose_name='Льготы')

    class Meta:
        verbose_name = 'Акаунт'
        verbose_name_plural = 'Акаунты'
        
    def __str__(self):
        return f"{self.name_l} {str(self.name_f)[0]}.\
            {str(self.patronymic)[0]}. ({self.phone})"
from rest_framework import serializers
from . import models


class AccountSerializer(serializers.ModelSerializer):
    """Сериализация акаунта, без логина и пароля."""
    class Meta:
        model = models.Account
        fields = ('id', 'name_f', 'name_l',
                  'patronymic', 'gender_id', 'educational_form',
                  'parent_mother', 'parent_father', 'citizenship',
                  'uin', 'address', 'city',
                  'country', 'phone', 'email',
                  'privileges', 'group')
        depth = 1


class AuthSerializer(serializers.ModelSerializer):
    """Сериализация запроса от пользователя на проверку логина и пароля."""
    class Meta:
        model = models.Account
        fields = ('login', 'password')
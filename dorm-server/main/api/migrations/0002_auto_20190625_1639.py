# Generated by Django 2.2.2 on 2019-06-25 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Акаунт', 'verbose_name_plural': 'Акаунты'},
        ),
        migrations.AlterModelOptions(
            name='dorm',
            options={'verbose_name': 'Общежитие', 'verbose_name_plural': 'Общежития'},
        ),
        migrations.AlterModelOptions(
            name='educationalform',
            options={'verbose_name': 'Форма обучения', 'verbose_name_plural': 'Формы обучения'},
        ),
        migrations.AlterModelOptions(
            name='floor',
            options={'verbose_name': 'Этаж общежития', 'verbose_name_plural': 'Этажи общежитий'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name': 'Человеческий пол', 'verbose_name_plural': 'Человеческие пола'},
        ),
        migrations.AlterModelOptions(
            name='guardian',
            options={'verbose_name': 'Опекун', 'verbose_name_plural': 'Опекуны'},
        ),
        migrations.AlterModelOptions(
            name='name',
            options={'verbose_name': 'Название', 'verbose_name_plural': 'Названия'},
        ),
        migrations.AlterModelOptions(
            name='orphanage',
            options={'verbose_name': 'Приют', 'verbose_name_plural': 'Приюты'},
        ),
        migrations.AlterModelOptions(
            name='parent',
            options={'verbose_name': 'Родитель', 'verbose_name_plural': 'Родители'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Отчёт', 'verbose_name_plural': 'Отчёты'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Заявление', 'verbose_name_plural': 'Заявления'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AddField(
            model_name='orphanage',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Название приюта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='account',
            name='children',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество детей                                                      в семье'),
        ),
        migrations.AlterField(
            model_name='account',
            name='citizenship',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Гражданство'),
        ),
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='account',
            name='educational_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.EducationalForm', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Gender', verbose_name='Человеческий пол'),
        ),
        migrations.AlterField(
            model_name='account',
            name='group',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='account',
            name='guardian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Guardian', verbose_name='Опекун'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name_f',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name_l',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='account',
            name='orphanage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Orphanage', verbose_name='Приют'),
        ),
        migrations.AlterField(
            model_name='account',
            name='parent_father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_father', to='api.Parent', verbose_name='Папа'),
        ),
        migrations.AlterField(
            model_name='account',
            name='parent_mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_mother', to='api.Parent', verbose_name='Мама'),
        ),
        migrations.AlterField(
            model_name='account',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='account',
            name='privileges',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Льготы'),
        ),
        migrations.AlterField(
            model_name='account',
            name='student_id',
            field=models.IntegerField(verbose_name='ID студента'),
        ),
        migrations.AlterField(
            model_name='account',
            name='uin',
            field=models.CharField(max_length=100, verbose_name='ИИН или номер паспорта'),
        ),
        migrations.AlterField(
            model_name='dorm',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Name', verbose_name='Название общежития'),
        ),
        migrations.AlterField(
            model_name='educationalform',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название формы обучения'),
        ),
        migrations.AlterField(
            model_name='floor',
            name='dorm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Dorm', verbose_name='Общежитие'),
        ),
        migrations.AlterField(
            model_name='floor',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Номер этажа'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Name', verbose_name='Название чел. пола'),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='name_f',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='name_l',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='name',
            name='en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст на английском'),
        ),
        migrations.AlterField(
            model_name='name',
            name='kz',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст на казахском'),
        ),
        migrations.AlterField(
            model_name='name',
            name='ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст на русском'),
        ),
        migrations.AlterField(
            model_name='orphanage',
            name='address',
            field=models.CharField(max_length=140, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='orphanage',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='name_f',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='name_l',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='report',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account', verbose_name='Акаунт'),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_residence',
            field=models.DateField(verbose_name='Дата заселения'),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='report',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Room', verbose_name='Комната'),
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Status', verbose_name='Статус отчёта'),
        ),
        migrations.AlterField(
            model_name='request',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account', verbose_name='Акаунт'),
        ),
        migrations.AlterField(
            model_name='request',
            name='active',
            field=models.IntegerField(verbose_name='Слушатель активности'),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_residence',
            field=models.DateField(verbose_name='Дата заселения'),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='request',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Room', verbose_name='Комната'),
        ),
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Floor', verbose_name='Этаж комнаты'),
        ),
        migrations.AlterField(
            model_name='room',
            name='max',
            field=models.PositiveIntegerField(verbose_name='Макс.                                         количество людей в комнате'),
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Номер комнаты'),
        ),
        migrations.AlterField(
            model_name='room',
            name='symbol',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Символ комнаты'),
        ),
        migrations.AlterField(
            model_name='status',
            name='active',
            field=models.IntegerField(verbose_name='Значение статуса'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Name', verbose_name='Название статуса'),
        ),
    ]
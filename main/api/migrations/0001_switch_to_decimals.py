# Generated by Django 2.2.3 on 2019-07-03 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, verbose_name='Логин')),
                ('password', models.CharField(max_length=255, verbose_name='Пароль')),
                ('name_f', models.CharField(max_length=100, verbose_name='Имя')),
                ('name_l', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('group', models.CharField(blank=True, max_length=10, null=True, verbose_name='Группа')),
                ('children', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество детей                                                      в семье')),
                ('student_id', models.IntegerField(verbose_name='ID студента')),
                ('citizenship', models.CharField(blank=True, max_length=100, null=True, verbose_name='Гражданство')),
                ('uin', models.CharField(max_length=100, verbose_name='ИИН или номер паспорта')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефонный номер')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта')),
                ('privileges', models.CharField(blank=True, max_length=255, null=True, verbose_name='Льготы')),
            ],
            options={
                'verbose_name': 'аккаунт',
                'verbose_name_plural': 'аккаунты',
            },
        ),
        migrations.CreateModel(
            name='Dorm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Общежитие',
                'verbose_name_plural': 'Общежития',
            },
        ),
        migrations.CreateModel(
            name='EducationalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название формы обучения')),
            ],
            options={
                'verbose_name': 'Форма обучения',
                'verbose_name_plural': 'Формы обучения',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Номер этажа')),
                ('dorm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Dorm', verbose_name='Общежитие')),
            ],
            options={
                'verbose_name': 'Этаж общежития',
                'verbose_name_plural': 'Этажи общежитий',
            },
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_f', models.CharField(max_length=100, verbose_name='Имя')),
                ('name_l', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефонный номер')),
            ],
            options={
                'verbose_name': 'Опекун',
                'verbose_name_plural': 'Опекуны',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст на русском')),
                ('kz', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст на казахском')),
                ('en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст на английском')),
            ],
            options={
                'verbose_name': 'Название',
                'verbose_name_plural': 'Названия',
            },
        ),
        migrations.CreateModel(
            name='Orphanage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название приюта')),
                ('address', models.CharField(max_length=140, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефонный номер')),
            ],
            options={
                'verbose_name': 'Приют',
                'verbose_name_plural': 'Приюты',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_f', models.CharField(max_length=100, verbose_name='Имя')),
                ('name_l', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефонный номер')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.IntegerField(verbose_name='Значение статуса')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Name', verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Номер комнаты')),
                ('max', models.PositiveIntegerField(verbose_name='Макс.                                         количество людей в комнате')),
                ('symbol', models.CharField(blank=True, max_length=255, null=True, verbose_name='Символ комнаты')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Floor', verbose_name='Этаж комнаты')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.IntegerField(verbose_name='Слушатель активности')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('date_residence', models.DateField(verbose_name='Дата заселения')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account', verbose_name='аккаунт')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Room', verbose_name='Комната')),
            ],
            options={
                'verbose_name': 'Заявление',
                'verbose_name_plural': 'Заявления',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(verbose_name='Слушатель активности')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('date_residence', models.DateField(verbose_name='Дата заселения')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Account', verbose_name='аккаунт')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Room', verbose_name='Комната')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Status', verbose_name='Статус отчёта')),
            ],
            options={
                'verbose_name': 'Отчёт',
                'verbose_name_plural': 'Отчёты',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Name', verbose_name='Название чел. пола')),
            ],
            options={
                'verbose_name': 'Человеческий пол',
                'verbose_name_plural': 'Человеческие пола',
            },
        ),
        migrations.AddField(
            model_name='dorm',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Name', verbose_name='Название общежития'),
        ),
        migrations.AddField(
            model_name='account',
            name='educational_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.EducationalForm', verbose_name='Форма обучения'),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Gender', verbose_name='Человеческий пол'),
        ),
        migrations.AddField(
            model_name='account',
            name='guardian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Guardian', verbose_name='Опекун'),
        ),
        migrations.AddField(
            model_name='account',
            name='orphanage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Orphanage', verbose_name='Приют'),
        ),
        migrations.AddField(
            model_name='account',
            name='parent_father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_father', to='api.Parent', verbose_name='Папа'),
        ),
        migrations.AddField(
            model_name='account',
            name='parent_mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_mother', to='api.Parent', verbose_name='Мама'),
        ),
    ]

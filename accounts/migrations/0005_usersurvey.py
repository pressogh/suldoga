# Generated by Django 4.0.6 on 2022-08-12 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('S', '증류주'), ('B', '양조주'), ('M', '혼성주')], max_length=1)),
                ('sweet', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1)),
                ('alcohol', models.IntegerField(choices=[('L', 'LOW'), ('M', 'MID'), ('H', 'HIGH')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

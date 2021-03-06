# Generated by Django 2.2 on 2020-03-08 22:15

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20200211_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ussurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]

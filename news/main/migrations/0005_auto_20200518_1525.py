# Generated by Django 3.0.6 on 2020-05-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_trandingpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trandingpost',
            name='desc',
            field=models.TextField(max_length=70),
        ),
    ]

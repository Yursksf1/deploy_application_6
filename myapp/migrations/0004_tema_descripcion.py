# Generated by Django 3.2.15 on 2022-10-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_materia_new_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='tema',
            name='descripcion',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]

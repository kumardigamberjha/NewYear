# Generated by Django 4.2.4 on 2023-12-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0008_alter_formmodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='formmodel',
            name='kid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

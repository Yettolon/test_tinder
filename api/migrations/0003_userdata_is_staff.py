# Generated by Django 3.2 on 2022-03-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_userdata_male_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
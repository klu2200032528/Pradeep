# Generated by Django 4.2.6 on 2023-10-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Prefer not to say', 'Prefer not to say'), ('Female', 'Female')], max_length=100),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-01 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_counter_app', '0003_number_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='email',
            field=models.CharField(max_length=5),
        ),
    ]

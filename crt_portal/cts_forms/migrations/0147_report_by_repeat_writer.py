# Generated by Django 3.2.13 on 2022-06-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0146_formletterssent'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='by_repeat_writer',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.2.15 on 2022-09-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0153_reportsdata_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportsdata',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

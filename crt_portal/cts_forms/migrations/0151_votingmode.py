# Generated by Django 3.2.15 on 2022-08-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0150_routingsteponecontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotingMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toggle', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 2.2.18 on 2021-02-19 22:05

import cts_forms.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cts_forms', '0099_covid_form_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protectedclass',
            name='protected_class',
            field=models.CharField(blank=True, choices=[('age', 'Age'), ('disability', 'Disability (including temporary or recovered and including HIV and drug addiction)'), ('family_status', 'Family, marital, or parental status'), ('gender', 'Gender identity (including gender stereotypes)'), ('genetic', 'Genetic information (including family medical history)'), ('immigration', 'Immigration/citizenship status (choosing this will not share your status)'), ('language', 'Language'), ('national_origin', 'National origin (including ancestry and ethnicity)'), ('pregnancy', 'Pregnancy'), ('race/color', 'Race/color'), ('religion', 'Religion'), ('sex', 'Sex'), ('orientation', 'Sexual orientation'), ('none', 'None of these apply to me'), ('other', 'Other reason')], max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='protectedclass',
            name='value',
            field=models.CharField(blank=True, choices=[('age', 'Age'), ('disability', 'Disability (including temporary or recovered and including HIV and drug addiction)'), ('family_status', 'Family, marital, or parental status'), ('gender', 'Gender identity (including gender stereotypes)'), ('genetic', 'Genetic information (including family medical history)'), ('immigration', 'Immigration/citizenship status (choosing this will not share your status)'), ('language', 'Language'), ('national_origin', 'National origin (including ancestry and ethnicity)'), ('pregnancy', 'Pregnancy'), ('race/color', 'Race/color'), ('religion', 'Religion'), ('sex', 'Sex'), ('orientation', 'Sexual orientation'), ('none', 'None of these apply to me'), ('other', 'Other reason')], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='crt_reciept_year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name=django.core.validators.MaxValueValidator(2021)),
        ),
        migrations.AlterField(
            model_name='report',
            name='intake_format',
            field=models.CharField(choices=[('web', 'Web'), ('letter', 'Letter'), ('phone', 'Phone'), ('fax', 'Fax'), ('email', 'Email')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='last_incident_year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name=django.core.validators.MaxValueValidator(2021, message='Date can not be in the future.')),
        ),
        migrations.AlterField(
            model_name='report',
            name='primary_complaint',
            field=models.CharField(choices=[('voting', 'Voting rights or ability to vote affected'), ('workplace', 'Workplace discrimination or other employment-related problem'), ('housing', 'Housing discrimination or harassment'), ('education', 'Discrimination at a school, educational program or service, or related to receiving education'), ('police', 'Mistreated by police, correctional staff, or inmates'), ('commercial_or_public', 'Discriminated against in a commercial location or public place'), ('something_else', 'Something else happened')], default='', max_length=100),
        ),
        migrations.CreateModel(
            name='ReportAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments', validators=[cts_forms.validators.validate_file_attachment])),
                ('filename', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='cts_forms.Report')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

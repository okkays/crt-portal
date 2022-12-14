# Generated by Django 2.2.20 on 2021-05-06 15:57

from django.db import migrations, models

def assign_language(apps, schema_editor):
    ResponseTemplate = apps.get_model('cts_forms', 'ResponseTemplate')
    templates = ResponseTemplate.objects.all()

    for template in templates:
        if '(Spanish)' in template.title:
            template.language = 'es'
        elif '(Chinese Traditional)' in template.title:
            template.language = 'zh-hant'
        elif '(Chinese Simplified)' in template.title:
            template.language = 'zh-hans'
        elif '(Vietnamese)' in template.title:
            template.language = 'vi'
        elif '(Korean)' in template.title:
            template.language = 'ko'
        elif '(Tagalog)' in template.title:
            template.language = 'tl'
        else:
            template.language = 'en'

        template.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0110_korean_form_letters'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsetemplate',
            name='language',
            field=models.CharField(default='en', max_length=10),
            preserve_default=False,
        ),
        migrations.RunPython(assign_language)
    ]

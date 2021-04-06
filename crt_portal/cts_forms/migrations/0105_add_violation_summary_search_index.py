# Generated by Django 2.2.19 on 2021-03-24 17:08

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0104_add_report_search_vector'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='report',
            index=django.contrib.postgres.indexes.GinIndex(fields=['violation_summary_search_vector'], name='cts_forms_r_violati_cb9487_gin'),
        ),
    ]

# Generated by Django 2.2.12 on 2020-04-30 18:00

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0147_report_by_repeat_writer'),
    ]

    def forward(apps, schema_editor):
        """
            Set Disability Class Choice to correct field.
        """
        ProtectedClass = apps.get_model('cts_forms', 'ProtectedClass')
        for pc in ProtectedClass.objects.all():
            if pc.value == 'disability-including-temporary-or-recovery':
                pc.value = 'disability'
                pc.save()

    def reverse(apps, schema_editor):
        """
            Revert back to faulty value
        """
        ProtectedClass = apps.get_model('cts_forms', 'ProtectedClass')
        for pc in ProtectedClass.objects.all():
            if pc.value == 'disability':
                pc.value = 'disability-including-temporary-or-recovery'
                pc.save()

    operations = [
        migrations.RunPython(forward, reverse_code=reverse),
    ]

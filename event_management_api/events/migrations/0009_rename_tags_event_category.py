# Generated by Django 5.1.1 on 2024-10-04 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='tags',
            new_name='category',
        ),
    ]

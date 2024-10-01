# Generated by Django 5.1.1 on 2024-10-01 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_capacity_eventregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to='events.event'),
        ),
    ]

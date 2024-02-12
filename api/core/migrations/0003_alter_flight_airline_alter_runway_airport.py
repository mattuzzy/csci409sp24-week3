# Generated by Django 5.0.2 on 2024-02-12 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_airline_flight_runway'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flights', to='core.airline'),
        ),
        migrations.AlterField(
            model_name='runway',
            name='airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runways', to='core.airport'),
        ),
    ]
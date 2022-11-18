# Generated by Django 4.1.3 on 2022-11-18 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flightinstance',
            options={'ordering': ['departure'], 'permissions': (('can_list_report', 'List report'), ('can_arrive_report', 'Arrive airport report'), ('can_departure_report', 'Departure airport report'), ('can_status_report', 'Flight Status report'))},
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='flight.airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='flight.airport'),
        ),
        migrations.AlterField(
            model_name='flightinstance',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instance', to='flight.flight'),
        ),
        migrations.AlterField(
            model_name='flightinstance',
            name='status',
            field=models.CharField(choices=[('Scheduled', 'Scheduled'), ('Onbording', 'Onbording'), ('Delayed', 'Delayed'), ('Departed', 'Departed'), ('In Air', 'In Air'), ('Expected', 'Expected'), ('Diverted', 'Diverted'), ('Recovery', 'Recovery'), ('Landed', 'Landed'), ('Arrived', 'Arrived'), ('Cancelled', 'Cancelled'), ('No Takeoff Info', 'No Takeoff Info - Call Airline'), ('Past Flight', 'Past Flight')], default='Scheduled', max_length=32),
        ),
    ]

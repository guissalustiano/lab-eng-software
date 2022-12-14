# Generated by Django 4.1.3 on 2022-11-25 17:53

from django.conf import settings
from django.db import migrations
from django.contrib.auth.management import create_permissions

def create_users(apps, editor):

    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None

    Permission = apps.get_model("auth.Permission")
    User = apps.get_model(settings.AUTH_USER_MODEL)

    admin_ = User.objects.create_superuser('admin', 'admin@mail.com', '1234')
    
    manager_ = User.objects.create_user('manager', 'manager@mail.com', '1234')
    operator_ = User.objects.create_user('operator', 'operator@mail.com', '1234')
    pilot_ = User.objects.create_user('pilot', 'pilot@mail.com', '1234')
    
    for codename in ['can_list_report','can_arrive_report','can_departure_report','can_status_report']:
        permission = Permission.objects.get(codename=codename)
        manager_.user_permissions.add(permission)

    for codename in ['change_flight','add_flight','view_flight','change_flightinstance','add_flightinstance','view_flightinstance']:
        permission = Permission.objects.get(codename=codename)
        operator_.user_permissions.add(permission)

    for codename in ['view_flight', 'change_flight', 'view_flightinstance', 'change_flightinstance']:
            permission = Permission.objects.get(codename=codename)
            pilot_.user_permissions.add(permission)

class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users, migrations.RunPython.noop),
    ]

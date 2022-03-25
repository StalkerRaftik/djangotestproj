from django.db import migrations, models
from django.contrib.auth import get_user_model


def create_superuser(apps, schema_editor):
    apps.get_model('auth', 'User').objects.create_superuser(
        'admin',
        'admin@myproject.com',
        'admin'
    )


class Migration(migrations.Migration):
    dependencies = [
        ('djangoproj', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, migrations.RunPython.noop),
    ]

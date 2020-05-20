from django.contrib.auth.hashers import make_password
from django.db import migrations


def add_user(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    User = apps.get_model('crud', 'User')
    new_user = User.objects.create(email='daniktarasov@gmail.com', password="")
    new_user.password = make_password("!`:V=C6-wVh=\ED")
    new_user._password = "!`:V=C6-wVh=\ED"
    new_user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('crud', '0002_auto_20200416_1723')
    ]

    operations = [
        migrations.RunPython(add_user)
    ]

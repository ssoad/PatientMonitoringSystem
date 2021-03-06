# Generated by Django 3.1.7 on 2021-03-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceController', '0002_devices_ip_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP_ADDRESS', models.GenericIPAddressField()),
            ],
        ),
        migrations.DeleteModel(
            name='Devices',
        ),
    ]

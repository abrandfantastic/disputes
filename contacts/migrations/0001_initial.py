# Generated by Django 2.0.6 on 2018-06-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.TextField(max_length=100)),
                ('from_email', models.CharField(max_length=250)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IOC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, null=True)),
                ('domain', models.CharField(max_length=100, null=True)),
                ('noticed_date', models.CharField(max_length=50, null=True)),
                ('source', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=244)),
                ('Name', models.CharField(max_length=244)),
                ('Message', models.CharField(max_length=244)),
                ('Subject', models.CharField(max_length=244)),
            ],
        ),
    ]

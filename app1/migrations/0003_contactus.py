# Generated by Django 3.2.4 on 2021-08-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_login_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('full_name', models.CharField(max_length=50)),
                ('umail', models.CharField(max_length=50)),
                ('qry', models.CharField(max_length=500)),
            ],
        ),
    ]
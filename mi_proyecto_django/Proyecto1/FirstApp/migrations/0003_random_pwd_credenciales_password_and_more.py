# Generated by Django 4.2.4 on 2023-09-22 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_credenciales'),
    ]

    operations = [
        migrations.CreateModel(
            name='random_pwd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default='user123@hotmail.com', max_length=50)),
                ('password', models.CharField(default='a35hfgssrDa4tasda2', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='credenciales',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='credenciales',
            name='usuario',
            field=models.CharField(default='user123@hotmail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='productos',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='productos',
            name='peso',
            field=models.IntegerField(default=0),
        ),
    ]

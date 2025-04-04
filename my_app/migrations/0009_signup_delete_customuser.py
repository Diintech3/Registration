# Generated by Django 5.1.6 on 2025-03-31 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_alter_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('Password', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('Mobile', models.BigIntegerField(default='', null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
            ],
        ),
    ]

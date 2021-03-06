# Generated by Django 3.2.9 on 2021-12-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.CharField(max_length=264)),
                ('no_of_classes', models.PositiveIntegerField()),
                ('isMiddleSchool', models.BooleanField(default=False)),
                ('established_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

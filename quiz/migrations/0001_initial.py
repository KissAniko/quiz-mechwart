# Generated by Django 4.2.7 on 2023-11-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer1', models.CharField(max_length=255)),
                ('answer1_is_true', models.BooleanField(default=False)),
                ('answer2', models.CharField(max_length=255)),
                ('answer2_is_true', models.BooleanField(default=False)),
                ('answer3', models.CharField(max_length=255)),
                ('answer3_is_true', models.BooleanField(default=False)),
                ('answer4', models.CharField(max_length=255)),
                ('answer4_is_true', models.BooleanField(default=False)),
            ],
        ),
    ]

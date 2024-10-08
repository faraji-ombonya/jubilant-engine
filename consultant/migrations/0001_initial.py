# Generated by Django 5.0.4 on 2024-04-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_disease', models.CharField(blank=True, max_length=10, null=True)),
                ('bmi', models.IntegerField()),
                ('smoking', models.CharField(max_length=10)),
                ('alcohol_drinking', models.CharField(max_length=10)),
                ('stroke', models.CharField(max_length=10)),
                ('physical_health', models.IntegerField()),
                ('mental_health', models.IntegerField()),
                ('diff_walking', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('age_category', models.CharField(max_length=10)),
                ('race', models.CharField(max_length=10)),
                ('diabetic', models.CharField(max_length=10)),
                ('physical_activity', models.CharField(max_length=10)),
                ('gen_health', models.CharField(max_length=10)),
                ('sleep_time', models.IntegerField()),
                ('asthma', models.CharField(max_length=10)),
                ('kidney_disease', models.CharField(max_length=10)),
                ('skin_cancer', models.CharField(max_length=10)),
            ],
        ),
    ]

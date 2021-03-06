# Generated by Django 3.0.4 on 2021-01-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_end', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dataa',
            fields=[
                ('s_no', models.IntegerField(primary_key=True, serialize=False)),
                ('entity', models.CharField(blank=True, default=False, max_length=50)),
                ('total_count', models.IntegerField(default=True)),
                ('entity_sections', models.CharField(blank=True, default=False, max_length=100)),
                ('organisation_name', models.CharField(blank=True, default=True, max_length=100)),
                ('doctor_name', models.CharField(blank=True, default=True, max_length=100)),
                ('recommended_coding_system', models.CharField(blank=True, default=True, max_length=30)),
                ('recommended_code', models.CharField(blank=True, default=True, max_length=30)),
                ('recommended_token', models.IntegerField(default=True)),
                ('is_recommended', models.BooleanField(default=True)),
                ('coding_system', models.CharField(blank=True, default=True, max_length=10)),
                ('code', models.CharField(max_length=100)),
                ('corrected_code_corrected_token', models.CharField(blank=True, default=True, max_length=100)),
                ('applicable_sections', models.CharField(blank=True, default=True, max_length=100)),
                ('is_submit', models.BooleanField(default=True)),
                ('is_verify', models.BooleanField(default=True)),
                ('flag_for_discussion', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'after_lockdown',
            },
        ),
        migrations.DeleteModel(
            name='data',
        ),
    ]

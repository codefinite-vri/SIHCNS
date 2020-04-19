# Generated by Django 3.0.4 on 2020-04-17 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datisdlogs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=30)),
                ('remarks', models.CharField(db_column='Remarks', max_length=100)),
                ('date', models.DateField(db_column='Date')),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'datisdlogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Datiswlogs',
            fields=[
                ('logs_id', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.CharField(db_column='Remarks', max_length=100)),
                ('value', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'datiswlogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dscndlogs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'dscndlogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vhfdlogs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'vhfdlogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vhfmlogs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_id', models.IntegerField()),
                ('value', models.CharField(max_length=30)),
                ('remarks', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'vhfmlogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vhfylogs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'vhfylogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mcdo',
            fields=[
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='login.Employee')),
                ('topic', models.CharField(max_length=50)),
                ('dop', models.DateTimeField(db_column='DOP')),
                ('content', models.TextField()),
                ('doa', models.DateTimeField(blank=True, db_column='DOA', null=True)),
            ],
            options={
                'db_table': 'mcdo',
                'managed': False,
            },
        ),
    ]
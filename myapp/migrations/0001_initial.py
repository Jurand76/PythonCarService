# Generated by Django 4.2.5 on 2023-09-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('codename', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, unique=True)),
                ('first_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150)),
                ('last_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150)),
                ('email', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Czesci',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50)),
                ('cena_zakupu', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ilosc', models.IntegerField()),
            ],
            options={
                'db_table': 'czesci',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('object_repr', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
                ('model', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Samochody',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('marka', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30)),
                ('model', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50)),
                ('wersja', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True)),
                ('nrrej', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=20, null=True)),
            ],
            options={
                'db_table': 'samochody',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wlasciciele',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imie', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30)),
                ('nazwisko', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=30)),
                ('adres', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=80, null=True)),
                ('telefon', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=20, null=True)),
                ('email', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=60, null=True)),
            ],
            options={
                'db_table': 'wlasciciele',
                'managed': False,
            },
        ),
    ]

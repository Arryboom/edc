# Generated by Django 2.2.6 on 2019-10-23 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('passwd', models.CharField(blank=True, max_length=60, null=True)),
                ('hashw', models.CharField(blank=True, max_length=1000, null=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('tknfile', models.FileField(blank=True, null=True, upload_to='')),
                ('first', models.CharField(blank=True, max_length=32, null=True)),
                ('last', models.CharField(blank=True, max_length=32, null=True)),
                ('role', models.CharField(blank=True, max_length=32, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='eventinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.CharField(blank=True, max_length=30, null=True)),
                ('poc', models.TextField(blank=True, null=True)),
                ('auth', models.TextField(blank=True, null=True)),
                ('unatuh', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=32)),
                ('network', models.CharField(blank=True, max_length=50, null=True)),
                ('users', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='oplog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('stop_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('src_host', models.CharField(max_length=100)),
                ('src_ip', models.CharField(max_length=32)),
                ('src_port', models.CharField(blank=True, max_length=15, null=True)),
                ('dst_host', models.CharField(max_length=100)),
                ('dst_ip', models.CharField(max_length=32)),
                ('dst_port', models.CharField(max_length=15)),
                ('piv_host', models.CharField(blank=True, max_length=100, null=True)),
                ('piv_ip', models.CharField(blank=True, max_length=32, null=True)),
                ('piv_port', models.CharField(blank=True, max_length=15, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('tool', models.CharField(max_length=100)),
                ('cmds', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('result', models.CharField(max_length=100, null=True)),
                ('output', models.TextField(blank=True, null=True)),
                ('scrsht', models.FileField(blank=True, null=True, upload_to='')),
                ('mods', models.CharField(blank=True, max_length=200, null=True)),
                ('exfil', models.FileField(blank=True, null=True, upload_to='')),
                ('comments', models.TextField(blank=True, null=True)),
                ('operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

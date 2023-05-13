# Generated by Django 4.1.7 on 2023-03-04 19:07

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
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FoundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('claimed_date', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('claimed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claimed_user', to=settings.AUTH_USER_MODEL)),
                ('founded_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='founded_item_user', to=settings.AUTH_USER_MODEL)),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='lost_item_report.itemcategory')),
            ],
        ),
    ]
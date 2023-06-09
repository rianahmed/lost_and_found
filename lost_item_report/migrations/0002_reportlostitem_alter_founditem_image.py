# Generated by Django 4.1.7 on 2023-03-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost_item_report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportLostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('date_lost', models.DateTimeField()),
                ('reporter_name', models.CharField(max_length=255)),
                ('reporter_phone', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='founditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

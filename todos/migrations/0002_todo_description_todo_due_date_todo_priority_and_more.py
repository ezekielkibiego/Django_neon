# Generated by Django 4.2.10 on 2024-02-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.CharField(max_length=200),
        ),
    ]

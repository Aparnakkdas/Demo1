# Generated by Django 3.2.12 on 2022-03-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='pics')),
                ('decs1', models.TextField()),
            ],
        ),
    ]
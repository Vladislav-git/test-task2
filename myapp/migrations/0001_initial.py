# Generated by Django 3.0.4 on 2020-03-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumberList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_list', models.TextField()),
                ('algorithm', models.CharField(choices=[('BubleSort', 'BubleSort'), ('InsertionSort', 'InsertionSort'), ('MergeSort', 'MergeSort')], max_length=20)),
                ('sorted_list', models.TextField()),
                ('file_field', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]

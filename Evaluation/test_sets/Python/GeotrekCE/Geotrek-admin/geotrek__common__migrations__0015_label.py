# Generated by Django 3.1.4 on 2020-12-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20201117_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictogram', models.FileField(blank=True, max_length=512, null=True, upload_to='upload', verbose_name='Pictogramme')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('advice', models.TextField(blank=True, verbose_name='Advice')),
                ('filter', models.BooleanField(default=False, help_text='Show this label as a filter in public portal', verbose_name='Filter')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
                'ordering': ['name'],
            },
        ),
    ]

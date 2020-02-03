# Generated by Django 2.2 on 2019-12-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_category', models.CharField(choices=[('Sports', 'Sports'), ('Politics', 'Politics'), ('Bollywood', 'Bollywood')], default='', max_length=50)),
                ('event_name', models.CharField(max_length=50)),
                ('event_image', models.ImageField(upload_to='images/')),
                ('event_price', models.IntegerField(default=0)),
                ('event_desc', models.TextField()),
            ],
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('response_at', models.DateTimeField()),
                ('sec_response_time', models.IntegerField()),
                ('url', models.TextField()),
                ('request_headers', models.TextField()),
                ('request_textfield', models.TextField()),
                ('response_code', models.TextField()),
                ('response_headers', models.TextField()),
                ('response', models.TextField()),
            ],
        ),
    ]

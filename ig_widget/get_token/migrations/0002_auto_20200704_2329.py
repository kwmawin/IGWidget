# Generated by Django 3.0.5 on 2020-07-04 23:29

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('get_token', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iguser',
            name='media_data',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='iguser',
            name='media_timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
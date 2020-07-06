# Generated by Django 3.0.4 on 2020-07-02 07:34

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_eventstream', '0004_event_read_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]

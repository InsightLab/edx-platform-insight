# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecohortssettings',
            name='always_cohort_inline_discussions',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_recordanswer_story_p1_recordanswer_story_p2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordanswer',
            name='recent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-23 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0002_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('NS', 'News'), ('AC', 'Article')], default='NS', max_length=2),
        ),
    ]

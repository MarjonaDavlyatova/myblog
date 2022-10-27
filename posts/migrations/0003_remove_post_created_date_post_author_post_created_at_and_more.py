# Generated by Django 4.1.2 on 2022-10-27 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_post_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-22 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_comments_comment_alter_like_is_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='user_post',
        ),
        migrations.AddField(
            model_name='hashtag',
            name='user_post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tags', to='posts.post', verbose_name='Post'),
            preserve_default=False,
        ),
    ]

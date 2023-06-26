# Generated by Django 4.2.2 on 2023-06-25 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_hashtag_user_post_hashtag_user_post'),
        ('accounts', '0003_account_is_active'),
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtagfollow',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='hashtagfollow',
            name='tag',
        ),
        migrations.AddField(
            model_name='hashtagfollow',
            name='follower',
            field=models.ManyToManyField(related_name='tag_followers', to='accounts.account', verbose_name='Follower'),
        ),
        migrations.AddField(
            model_name='hashtagfollow',
            name='tag',
            field=models.ManyToManyField(related_name='followed_tags', to='posts.hashtag', verbose_name='Hashtag'),
        ),
    ]
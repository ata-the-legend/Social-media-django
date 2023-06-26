# Generated by Django 4.2.2 on 2023-06-19 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('posts', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followees', to='accounts.account', verbose_name='Followee')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='accounts.account', verbose_name='Follower')),
            ],
            options={
                'verbose_name': 'UserFollow',
                'verbose_name_plural': 'UserFollows',
            },
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='HashtagFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='Follower')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.hashtag', verbose_name='Hashtag')),
            ],
            options={
                'verbose_name': 'HashtagFollow',
                'verbose_name_plural': 'HashtagFollows',
            },
        ),
    ]
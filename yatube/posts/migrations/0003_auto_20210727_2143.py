# Generated by Django 2.2.9 on 2021-07-27 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210725_0758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=1, max_length=70, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Group'),
        ),
    ]

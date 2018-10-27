# Generated by Django 2.0.3 on 2018-10-26 16:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('merlin', '0002_reliefcamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('contact', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

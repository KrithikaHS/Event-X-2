# Generated by Django 4.2.20 on 2025-04-05 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('venue', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='event_images/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='users.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

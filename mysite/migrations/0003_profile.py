# Generated by Django 4.0.4 on 2023-09-10 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField(default=160)),
                ('male', models.BooleanField(default=False)),
                ('website', models.URLField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mysite.user')),
            ],
        ),
    ]

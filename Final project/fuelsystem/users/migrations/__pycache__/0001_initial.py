# Generated by Django 4.0.4 on 2022-04-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AL', 'AL'), ('AK', 'AK'), ('AR', 'AR'), ('AZ', 'AZ'), ('CA', 'CA'), ('CT', 'CT'), ('CO', 'CO'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('IA', 'IA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN')], default='AL', max_length=20)),
                ('zip', models.IntegerField(max_length=9)),
            ],
        ),
    ]

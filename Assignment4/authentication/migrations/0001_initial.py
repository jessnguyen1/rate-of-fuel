# Generated by Django 4.0.3 on 2022-04-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fuelQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userGallonsRequested', models.IntegerField()),
                ('userDeliveryDate', models.DateTimeField()),
                ('userSuggestedPrice', models.IntegerField()),
                ('userTotalPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=50)),
                ('userPassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileManagemenent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('userState', models.CharField(max_length=2)),
            ],
        ),
    ]

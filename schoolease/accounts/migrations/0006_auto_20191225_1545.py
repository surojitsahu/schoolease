# Generated by Django 3.0.1 on 2019-12-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191225_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='CCTV1',
            field=models.BooleanField(default=False, verbose_name='Not Present'),
        ),
        migrations.AddField(
            model_name='school',
            name='Damege_to_Property',
            field=models.BooleanField(default=False, verbose_name='Damege_to_Property'),
        ),
        migrations.AddField(
            model_name='school',
            name='Do_you_support_any_Extra_Activities',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Facilities_Provided',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Fee_Structure',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Fighting',
            field=models.BooleanField(default=False, verbose_name='Fighting'),
        ),
        migrations.AddField(
            model_name='school',
            name='Glorious_Alumini_Network',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Late_Arrivels',
            field=models.BooleanField(default=False, verbose_name='Late_Arrivels'),
        ),
        migrations.AddField(
            model_name='school',
            name='Major_Achivements',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Misbehaving',
            field=models.BooleanField(default=False, verbose_name='Misbehaving'),
        ),
        migrations.AddField(
            model_name='school',
            name='Our_Teachings_Ideology',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Our_future_Plans_Development',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Principle_Message',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Qualification_Details_of_Teachers',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='Sports_Played',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='upload_video',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
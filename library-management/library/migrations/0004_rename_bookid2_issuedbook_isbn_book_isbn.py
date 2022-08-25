# Generated by Django 4.0.5 on 2022-08-21 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rename_bookid_issuedbook_bookid2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbook',
            old_name='bookid2',
            new_name='isbn',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-30 10:45

from django.db import migrations
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shop.Category'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shop.Product'),
        ),
    ]

# Generated by Django 2.0.7 on 2018-12-18 15:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='workflowlevel2_uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, help_text='Unique ID to relate back to Bifrost workflow', max_length=255, unique=True, verbose_name='WorkflowLevel2 UUID'),
        ),
    ]
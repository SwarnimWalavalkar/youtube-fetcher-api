import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('published_on', models.DateTimeField()),
                ('thumbnail_url', models.CharField(max_length=100)),
                ('video_url', models.CharField(max_length=100)),
            ]
        ),
    ]

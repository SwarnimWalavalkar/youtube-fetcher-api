from datetime import datetime, timedelta, timezone
import traceback
from django.core.management.base import BaseCommand
from django.conf import settings
from googleapiclient.discovery import build, HttpError
from videos.models import Video


class Command(BaseCommand):
    help = "A description of the command"

    def handle(self, *args, **options):
        self.stdout.write("Running the fetch_videos job...")
        API_KEYS = settings.YT_API_KEYS

        workingKeyIndex = 0
        noOfChanges = 0
        developerKey = API_KEYS[workingKeyIndex]
        foundWorkingKey = False

        while (not foundWorkingKey):
            try:
                api = build('youtube', 'v3', developerKey=developerKey)
                foundWorkingKey = True

                date = datetime.now(timezone.utc) - timedelta(minutes=10)
                res = api.search().list(q="news", part="snippet",
                                        maxResults=10, type="video", publishedAfter=date.isoformat()).execute()["items"]
                videos = []

                for item in res:
                    try:
                        videos.append(Video(
                            title=item["snippet"]["title"], description=item["snippet"]["description"], published_on=item["snippet"]["publishedAt"], video_url=f"https://youtu.be/{item['id']['videoId']}", thumbnail_url=item["snippet"]["thumbnails"]["default"]["url"]))
                    except Exception:
                        self.stderr.write(traceback.format_exc())

                for video in videos:
                    video.save()
            except HttpError:
                if noOfChanges > len(API_KEYS)-1:
                    raise Exception("NO_VALID_API_KEY")

                workingKeyIndex = min(workingKeyIndex+1, len(API_KEYS)-1)
                developerKey = API_KEYS[workingKeyIndex]
                self.stdout.write("API Key Changed")
                noOfChanges += 1
                continue

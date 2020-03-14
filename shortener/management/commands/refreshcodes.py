from django.core.management.base import BaseCommand, CommandError
from shortener.models import UssUrl

class Command(BaseCommand):
    help = 'Refreshes all UssUrl short codes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

        

    def handle(self, *args, **options):
        return UssUrl.objects.refresh_shortcodes(items=options['items'])
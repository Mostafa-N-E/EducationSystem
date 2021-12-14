from django.core.management.base import BaseCommand, CommandError
from persons.models import Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('student_id', nargs='+', type=int)
        parser.add_argument('student_username', nargs='+', type=str)

        # Named (optional) arguments
        parser.add_argument(
            '--clean_select_class',
            action='store_true',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        # ...
        if options['delete']:
            Student.delete()

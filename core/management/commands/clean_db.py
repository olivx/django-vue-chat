from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--all', '-a',
                            action='store_true',
                            help='deleta tudo, zera o banco.')
   
    def handle(self, *args, **options):
        # deleting user
        users = User.objects.filter(is_superuser=False)
        print(users.count() , 'usarios deletados')
        users.delete()

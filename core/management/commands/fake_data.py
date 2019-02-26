import re
import os
import random
from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    def __init__(self):
        self.fake = Faker('pt_BR')

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int,
                        help='how many users you want creating.')



    def handle(self, *args, **options):
        # create user 
        many_users = options['n'] if options['n'] else 50
        if User.objects.count() <= 100:
            user_list = []
            for _ in range(many_users):
                username_email = self.fake.ascii_free_email()
                while len(username_email) >= 30:
                    username_email = self.fake.ascii_free_email()
                data = {
                    'first_name': self.fake.first_name(),
                    'last_name': self.fake.last_name(),
                    'username': username_email,
                    'email': username_email,
                    'password':'hashedPassword1!',
                    'is_active':True,
                }
                user_list.append(User(**data))
            User.objects.bulk_create(user_list)
            print(f'{many_users} Random Users created! , you have {User.objects.count()} in totla')
        else:
            print('max user was created to teste...')

        
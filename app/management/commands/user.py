from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        email = input("Email:\n>")
        password = input("Password:\n>")
        
        
        user = User.objects.create(email=email, is_superuser=True, is_staff=True, is_admin=True, role="admin")
        user.set_password(password)
        user.save()
        
        self.stdout.write(self.style.SUCCESS("Successfully added superuser"))
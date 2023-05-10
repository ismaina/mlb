from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
 
class Command(BaseCommand):
    """
    Create a superuser if none exist
    Example:
        manage.py createsuperuser_if_none_exists --user=admin --password=changeme
    """
    help = 'create superuser'
 
    # def add_arguments(self, parser):
    #     parser.add_argument("--user", required=True)
    #     parser.add_argument("--password", required=True)
    #     parser.add_argument("--email", default="admin@example.com")
 
    def handle(self, *args, **options):
 
        User = get_user_model()
        if User.objects.filter(is_superuser=True).exists():
            print("Admin exists")
            return
        
        username = "admin"
        first_name = "admin"
        last_name = "admin"
        email = "ep@safaricom.co.ke"
        password = "armfulgoofinessreturnfolicunearthpurgingenforcerhandsfree"
 
        user =User.objects.create_superuser(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()

        profile = user.profile
        profile.role="analyst"
        profile.save()
        self.stdout.write(f'Local user "{username}" was created')
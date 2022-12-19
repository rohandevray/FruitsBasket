#creating the profile when user is created / register 
#signals
from django.db.models.signals import post_save, post_delete
#post_save triggers after a model is saved
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver #decorator
#sending mails
from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender,instance,created,**kwargs):
    # IMPORTANT : when user is created a profile for it will be generated 
    if created: #created is flag (true or false for new user)
        user = instance
        profile = Profile.objects.create(
            #auto fill info in profile when a user is created
            user = user, #auto connecting the user that triggers to its profile (user after equal is instance)
            username = user.username,
            email = user.email,
            name = user.first_name
        )
 #sending mails after registering to website
        subject = 'Welcome to FruitsBasket!'
        message = 'Thanks for choosing us!'

        send_mail(
             subject,
             message,
             settings.EMAIL_HOST_USER,
             [profile.email],
             fail_silently=False,
        )



post_save.connect(createProfile,sender=User) 
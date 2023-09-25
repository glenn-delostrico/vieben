from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    id_user = models.IntegerField()
    headline = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.webp') 
    location = models.CharField(max_length=100, blank=True)

    age = models.PositiveIntegerField(null=True, blank=True)
    
    # Choices for the sex field
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    
    # Choices for the looking_for_relationship field
    PENPAL = 'Penpal'
    FRIENDSHIP = 'Friendship'
    DATING = 'Dating'
    SHORT_TERM_RELATIONSHIP = 'Short Term Relationship'
    LONG_TERM_RELATIONSHIP = 'Long Term Relationship'
    
    LOOKING_FOR_CHOICES = [
        (PENPAL, 'Penpal'),
        (FRIENDSHIP, 'Friendship'),
        (DATING, 'Dating'),
        (SHORT_TERM_RELATIONSHIP, 'Short Term Relationship'),
        (LONG_TERM_RELATIONSHIP, 'Long Term Relationship'),
    ]
    looking_for_relationship = models.CharField(max_length=30, choices=LOOKING_FOR_CHOICES, blank=True)

    def __str__(self):
        return self.user.username
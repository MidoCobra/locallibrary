from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns


from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Kind(models.Model):
     

    sch_kind = (
        ('N', 'national'),
        ('I', 'international'),
        ('B', 'Both Sections')
    )
    school_kind =models.CharField(max_length=1, choices=sch_kind, blank=True, default='N', help_text='School type')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.school_kind
    
class Area(models.Model):

    name =  models.CharField(max_length=100)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Schools(models.Model):
    kind = models.ForeignKey('Kind', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    area = models.ForeignKey('Area', null =True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to = 'media/', default = 'media/mido.jpg')
    web_site = models.URLField(max_length=200, default= "http://www.schooladvisoregypt.com")


    class Meta:
        #i used this verbose to remove a weired extra 's' appeared in the admin side beside the title Schools
        verbose_name_plural = "Schools"

    # def __str__(self):
    #     """
    #     String for representing the Model object (in Admin site etc.)
    #     """
    #     return self.name    

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('school-detail', args=[str(self.id)])     

    def __str__(self):
        """
        String for representing the Model object
        String for representing the Model object (in Admin site etc.)
        """
        return '{0} ({1})'.format(self.name, self.kind)       



class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class SchoolReview(Review):
    school = models.ForeignKey(Schools, on_delete=models.SET_NULL, null=True)
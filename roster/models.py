from django.db import models

# Create your models here.

class Player(models.Model):
    number = models.IntegerField(unique=True, null=True, max_length=4, verbose_name="No.")
    firstname = models.TextField(null=False)
    class Meta(object):
        verbose_name_plural = "Players"
        ordering = ('lastname', 'number')
    
    def __unicode__(self):
        return self.lastname
    
    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)
    
    lastname = models.TextField(null=False)
    imgurl = models.TextField(null=True)
    dominant_hand = models.CharField(null=True, max_length=5)
    position = models.CharField(null=True, max_length=6)
    height = models.CharField(null=True, max_length=5, verbose_name="Height")
    weight = models.CharField(null=True, max_length=5, verbose_name="Weight")
    year = models.CharField(null=True, max_length=30)
    hometown = models.TextField(null=True, verbose_name="Hometown")
    home_long = models.TextField(null=True, verbose_name="Hometown Longitude")
    home_lat = models.TextField(null=True, verbose_name="Hometown Latitude")
    high_school = models.TextField(null=True, verbose_name="High School")
    batting_avg = models.CharField(null=True, max_length=5)
    gp_gs = models.CharField(null=True, max_length=5)
    at_bats = models.CharField(null=True, max_length=5)
    runs = models.CharField(null=True, max_length=5)
    hits = models.CharField(null=True, max_length=5)
    doubles = models.CharField(null=True, max_length=5)
    homeruns = models.CharField(null=True, max_length=5)
    rbi = models.CharField(null=True, max_length=5)
    total_bases = models.CharField(null=True, max_length=5)
    slugging = models.CharField(null=True, max_length=5)
    walks = models.CharField(null=True, max_length=5)
    strikeouts = models.CharField(null=True, max_length=5)
    on_base_percentage = models.CharField(null=True, max_length=5)
    assists = models.CharField(null=True, max_length=5)
    errors = models.CharField(null=True, max_length=5)
    story_junior = models.TextField(null=True)
    story_sophomore = models.TextField(null=True)
    story_freshman = models.TextField(null=True)
    story_highschool = models.TextField(null=True)
    story_personal = models.TextField(null=True)

    
    
    class Meta(object):
        ordering = ('number', 'position')
        
    def __unicode__(self):
        return self.lastname
    
    
    
class Coach(models.Model):
    firstname = models.TextField(null=True)
    lastname = models.TextField(null=True)
    
    class Meta(object):
        verbose_name_plural = "Coaches"
        ordering = ('lastname','coaching_age')
    
    def __unicode__(self):
        return self.lastname
    
    def save(self, *args, **kwargs):
        self.lastname = self.lastname()
        super(Coach, self).save(*args, **kwargs)

    title = models.TextField(null=True)
    story = models.TextField(null=True)
    coaching_age = models.IntegerField(null=True, max_length=2)

    
class Team(models.Model):
    name = models.TextField(unique=False)
    gender = models.TextField(unique=False)
    url = models.URLField(unique=False, max_length=400)
    roster_url = models.URLField(unique=False, max_length=400)
    
    class Meta(object):
        verbose_name_plural = "Teams"
        
    def __unicode__(self):
        return U'%s %s' %(self.name, self.gender)
        
    def save(self, *args, **kwargs):
        self.name = self.name.upper()   
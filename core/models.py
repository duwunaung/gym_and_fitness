from django.db import models

# Services (title, description, images)
class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.title
    
class Subscription(models.Model):
    title = models.CharField(max_length=150)
    amount = models.IntegerField()
    duration = models.IntegerField()
    count = models.CharField(max_length=50)
    fitness_classes = models.BooleanField(default=False)
    workout_program = models.BooleanField(default=False)
    certified_trainer = models.BooleanField(default=False)
    health_assessment = models.BooleanField(default=False)
    goal_setting = models.BooleanField(default=False)
    nutrition_consultation = models.BooleanField(default=False)
    registered_dietitian = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Fake_News(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="images", null=True)
    duration = models.IntegerField()
    author = models.CharField(max_length=100)
    comment_count = models.IntegerField()

    class Meta:
        verbose_name_plural = "News"
        
    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class Info(models.Model):
    phone = models.CharField(max_length=20)
    info = models.TextField()
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    tiktok = models.URLField()
    email = models.EmailField()
    address = models.TextField()
    website = models.URLField()

class Message(models.Model):
    email = models.EmailField()
    message = models.TextField()
    
    date = models.DateField(auto_now=True, null=True, editable=False)
    
    def __str__(self):
        return self.email
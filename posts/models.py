import uuid

from django.db import models



class Event(models.Model):
    CHOICES = (
        ('MARRIAGE' , 'marriage'),
        ('BIRTHDAY' , 'birthday'),
        ('FUNERAL' , 'funeral')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='events/',null=True, blank=True)
    event_type = models.CharField(max_length=255 ,choices=CHOICES)
    event_date = models.DateField(max_length=64)
    single_time = models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=18)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    # title = models.CharField(max_length=255)
    # event = models.ManyToManyField("posts.Event")
    # event_image = models.ImageField(upload_to="posts/")  
    # customer = models.ForeignKey("posts.Member", on_delete=models.CASCADE)
    # is_deleted = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.title

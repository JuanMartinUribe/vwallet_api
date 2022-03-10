from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class MainUser(models.Model):
    class MainUserObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all()
            
    
    objects = models.Manager()
    mainuserobjects = MainUserObjects()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    def __str__(self):
            return self.user.username 
class Pocket(models.Model):
    class PocketObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = 'available')
    options = (
        ('available','Available'),
        ('blocked','Blocked'),
    )
    name = models.CharField(max_length=250)
    quantity = models.DecimalField(max_digits=20,decimal_places=10)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,choices=options,default='available')

    main_user = models.ForeignKey(
        to = MainUser ,related_name='pockets',on_delete=models.CASCADE,default=1
    )
    objects = models.Manager()
    pocketobjects = PocketObjects()

    class Meta:
        ordering = ('-created_at',)
        def __str__(self):
            return self.name
    def __str__(self):
            return '%s: %d' % (self.name,self.quantity)     

from django.db import models
from django.urls import reverse

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=80, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    class Meta:
        unique_together = ('parent',)
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'


    def __str__(self):                          
        full_path = [self.name]         
        k = self.parent                          

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Pet(models.Model):

    """Model representing a specific pet"""
    id = models.AutoField(primary_key=True)

    # FK used because each pet can only belong to one animal, but each animal may have multiple pets
    animal = models.ForeignKey('Animal', on_delete=models.SET_NULL, null=True, blank=True)

    breeder = models.ForeignKey('Breeder', on_delete=models.SET_NULL, null=True)

    likes = models.TextField(max_length=1000 ,default="", help_text="A few things the pet likes")


    SALE_STATUS = (
        ('a', 'Available'),
        ('u', 'Unavailable'),
        ('r', 'Reserved'),
        ('s', 'Sold'),
    )

    status = models.CharField(
        max_length=1,
        choices=SALE_STATUS,
        blank=True,
        default='a',
        help_text='status of the pet',
    )
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this pet."""
        return reverse('pet-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.id}, {self.animal}'

class Breeder(models.Model):
    """Model representing supplier of the animal"""
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)

    def get_absolute_url(self):
        """Returns the url to access a particular breeder instance."""
        return reverse('breeder-detail', args=[str(self.id)])


    def __str__(self):
        return self.name

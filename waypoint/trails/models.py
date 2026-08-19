from django.db import models
from django.core.validators import MinValueValidator

class Park(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trail(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Difficult', 'Difficult'),
    ]

    name = models.CharField(max_length=100)
    distance_km = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    elevation_gain = models.IntegerField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    is_open = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)

    park = models.ForeignKey(Park, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
class TrailReport(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    trail = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report di {self.name} su {self.trail}"

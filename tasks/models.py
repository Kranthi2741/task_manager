from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Study', 'Study'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

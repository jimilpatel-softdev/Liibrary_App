from django.db import models
from django.utils import timezone
from datetime import timedelta

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book, related_name="loans", on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name="loans", on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)  # Changed to DateTimeField
    due_date = models.DateTimeField()  # Changed to DateTimeField
    return_date = models.DateTimeField(blank=True, null=True)  # Changed to DateTimeField

    def is_overdue(self):
        # Compare timezone-aware datetime objects
        if not self.return_date and self.due_date < timezone.now():
            return True
        return False

    def calculate_fine(self):
        # Calculate fine based on timezone-aware datetime objects
        if self.is_overdue():
            days_overdue = (timezone.now() - self.due_date).days
            return days_overdue * 5  # Fine: $5 per day
        return 0

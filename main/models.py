from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.
class Slot_Register(models.Model):
    distrubuter = models.CharField(max_length=30)
    movie_name = models.CharField(max_length=30)
    actor_name = models.CharField(max_length=30)
    screen_no = models.CharField(max_length=20,default="1")
    description = models.TextField(default="add description please")
    ticket_price = models.IntegerField()
    poster = models.ImageField(upload_to="posters/")
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.movie_name
    


class Book(models.Model):
    movie_name = models.CharField(max_length=30)
    actor_name = models.CharField(max_length=30)
    screen_no = models.CharField(max_length=20,default="1")
    ticket_price = models.IntegerField()
    description = models.TextField(default="add description please")
    poster = models.ImageField(upload_to="posters/")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.movie_name
    

class Days(models.Model):
    cinema = models.ForeignKey(Book,on_delete=models.CASCADE)
    day = models.DateField(default=True,null=True)

    def __str__(self):
        return str(self.day)


class Show(models.Model):
    movie = models.ForeignKey(Book,on_delete=models.CASCADE)
    date = models.ForeignKey(Days,on_delete=models.CASCADE)
    show_time = models.CharField(max_length=20)
    time = models.TimeField(null=True)

    def __str__(self) -> str:
        return f"{self.movie.movie_name} at {self.show_time} on {self.date.day}"
    

class BookedSeat(models.Model):
    book = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Booked Seat {self.seat_number} for {self.book.movie_name}"
    

class Timeings(models.Model):
    show_time = models.TimeField(null=True)


@receiver(post_save, sender=Slot_Register)
def create_book_from_slot_register(sender, instance, created, **kwargs):
    if created:
        Book.objects.create(
            movie_name=instance.movie_name,
            actor_name=instance.actor_name,
            screen_no=instance.screen_no,
            description=instance.description,
            ticket_price=instance.ticket_price,
            # Since ImageField needs special handling, we copy the file over manually
            poster=instance.poster,
            created_at=instance.created_at,
        )

    



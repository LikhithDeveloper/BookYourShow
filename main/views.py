from django.shortcuts import render
from .models import *
from datetime import datetime,timedelta


# Create your views here.

def book(request):
    queryset = Book.objects.all()
    context = {'booking': queryset}
    return render(request,"ui.html",context)
import datetime
def time(request,id):  
    today = datetime.date.today() 
    current_time = datetime.datetime.now().time()
    queryset = Book.objects.get(id=id) 
    dayset = Days.objects.get(day = today) 
    queryset1 = Show.objects.filter(movie = queryset , date = dayset)
    day = dayset.day
    x = []
    for i in queryset1:
        if i.time > current_time and i.date.day == today:
            x.append(i)
    print(x)
    context = {'movie':queryset,'timeing':x}
    return render(request,"book.html",context)

def tickets(request,id):
    queryset = Show.objects.get(id = id)
    name = queryset.movie.movie_name
    print(name)
    context = {'shows':queryset}
    print(queryset)

    return render(request,"tickets.html",context)

def movie(request):
    if request.method == "POST":
        data = request.POST
        distrubuter = data.get('distrubuter')
        movie_name = data.get('movie_name')
        actor_name = data.get('actor_name')
        screen_no = data.get('screen_no')
        description = data.get('description')
        ticket_price = data.get('ticket_price')
        poster = request.FILES.get('poster')      #for files
        day_1 = datetime.datetime.strptime(data.get('day_1'), '%Y-%m-%d')
        day_n = datetime.datetime.strptime(data.get('day_n'), '%Y-%m-%d')
        Slot_Register.objects.create(
            distrubuter = distrubuter,
            movie_name = movie_name,
            actor_name = actor_name,
            screen_no = screen_no,
            description = description,
            ticket_price = ticket_price,
            poster = poster
        )  
        queryset = Book.objects.get(movie_name = movie_name)  
        print(day_1)
        print(day_n)
        current_date = day_1
        end_date = day_n
        while current_date <= end_date:
            Days.objects.create(cinema = queryset,day = current_date)
            current_date += timedelta(days=1)
    queryset1 = Book.objects.all()
    queryset2 = Days.objects.all()
    queryset3 = Timeings.objects.all()
    for i in queryset1:
        for j in queryset2:
            for k in queryset3:
                if not Show.objects.filter(movie=i, date=j, show_time=k.show_time).exists() and j.cinema.movie_name == i.movie_name:
                    Show.objects.create(
                        movie = i,
                        date = j,
                        show_time = str(k.show_time),
                        time = k.show_time
                    )
    return render(request,"admin.html")
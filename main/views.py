from django.shortcuts import render,redirect
from .models import *
from datetime import datetime,timedelta
import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def book(request):
    queryset = Book.objects.all()
    print(queryset[0].poster)
    context = {'hooking': queryset}
    return render(request,"ux.html",context)

def date(request,id):
    today = datetime.date.today() 
    current_time = datetime.datetime.now().time()
    queryset = Book.objects.get(id=id)
    dayset = Days.objects.all()
    for i in dayset:
        if i.day < today:
            i.delete()
    dayset1 = Days.objects.filter(cinema = queryset)
    
    context = {'movie':queryset,'dates':dayset1}
    return render(request,"date.html",context)


def time(request,id):  
    today = datetime.date.today() 
   # print(today)
    current_time = datetime.datetime.now().time()
    dayset = Days.objects.get(id = id) 
   # print(dayset)
    name = dayset.cinema.movie_name
   # print(name)
    queryset = Book.objects.get(movie_name = name)
   # print(queryset)
    queryset1 = Show.objects.filter(movie = queryset , date = dayset)           
   # print(queryset1)
    day = dayset.day
   # print(day)
    x = []
    if day == today:
        for i in queryset1:
            print(i.date)
            if i.time > current_time and str(i.date) == str(today):
                x.append(i)
    else:
        x = queryset1

    context = {'movie':queryset,'timeing':x}
    return render(request,"book.html",context)

def tickets(request,id):
    queryset = Show.objects.get(id = id)
    queryset1 = BookedSeat.objects.filter(book = queryset)
    x = Total.objects.all()
    occupied_seats = [int(i.seat_number) for i in queryset1]
   # print(queryset1)
   # print(occupied_seats)
    seat_range = range(11, 81) 
    price = queryset.movie.ticket_price
   # print(price) 
    context = {'movies':queryset,'occupied':occupied_seats,'seat_range':seat_range}
    if request.method == "POST":
        selected_seats = request.POST.get('selected_seats')
        no_of_seats = request.POST.get('no_of_seats')
        #print(no_of_seats)
        #print(selected_seats)
        length = len(selected_seats)
        size = length // int(no_of_seats)
        parts = [selected_seats[i:i+size] for i in range(0, length, 2)]
        #print(parts)
        #print(len(parts))
        if len(parts) != int(no_of_seats):
            messages.warning(request, "Select the number of seats you selected")
            return redirect(f'/tickets/{id}')
        else:
            for i in parts:
                BookedSeat.objects.create(book =queryset,seat_number = int(i)) 
            messages.info(request,f"The selected seates are {parts} of {len(parts)*price} at {queryset.time} on {queryset.date.day}")
            return redirect(f'/tickets/{id}')


    
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
        poster = request.FILES.get('image')      #for files
        day_1 = datetime.datetime.strptime(data.get('day_1'), '%Y-%m-%d')
        day_n = datetime.datetime.strptime(data.get('day_n'), '%Y-%m-%d')
        print(request.POST)
        print(request.FILES )
        print(request.FILES.get('image') )

        print(poster)
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



def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(username=username, password=password)
         
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        elif username=="admin":
            return redirect('/movie')
        else:
            login(request, user)
            return redirect('/book/')
    return render(request, 'login.html')
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        user = User.objects.filter(username=username)
         
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully!")
        return redirect('/')
     
    # Render the registration page template (GET request)
    return render(request, 'register.html')

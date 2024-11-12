from django.shortcuts import render
import datetime

# Create your views here.
def nav_home(request):
    data = {'author' : 'Rahim', 'age': 20, 'birthday': datetime.datetime.now(), 'friends' : ['hasan', 'kamal', 'jamal'], 'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 200,
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 500,
        },
        {
            'id' : 3,
            'name' : 'C++',
            'fee' : 100,
        }
    ]}
    return render(request, 'app_home.html', context=data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


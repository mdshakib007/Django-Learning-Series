from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    data = {
        'id' : 1,
        'name' : 'Shakib',
        'age' : 21,
        'description' : 'hello, this is shakib, from bangladesh. currently learning django course! this is the learning file!',
        'birthday' : datetime.datetime.now(),
        'friends' : ['hasan', 'kamal', 'jamal'],
        'incomes' : [1, 2, 3, 4, 5],
        'courses' : [
            {
                'name' : 'Python',
                'fees' : 200
            },
            {
                'name' : 'Django',
                'fees' : 500
            },
            {
                'name' : 'Database',
                'fees' : 300
            }
        ]
    }
    return render(request, 'practice_app/home.html', context=data)

def about(request):
    return render(request, 'practice_app/about.html')

def contact(request):
    return render(request, 'practice_app/contact.html')
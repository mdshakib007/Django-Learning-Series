from django.shortcuts import render, redirect
from car.models import CarModel, CommentModel
from django.contrib.auth.models import User
from django.contrib import messages
from car.forms import CommentBox

def view_details_view(request, id):
    car = CarModel.objects.get(pk=id)
    comments = CommentModel.objects.filter(car=car).order_by('-created_at')
    
    if request.user.is_authenticated:
        form = CommentBox()  
        
        if request.method == 'POST':
            form = CommentBox(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.car = car
                comment.customer = request.user
                comment.save()
                messages.success(request, "Comment added successfully!")
                return redirect('view_details', id=id) 
        return render(request, 'car/view_details.html', {'car': car, 'form': form, 'comments': comments})

    return render(request, 'car/view_details.html', {'car': car, 'comments': comments})


def confirm_order_view(request, id):
    if request.user.is_authenticated:
        car = CarModel.objects.get(pk=id)
        
        if car.quantity < 1:
            messages.warning(request, "Failed to buy that car! Stock is unavailable.")
            return redirect('home')

        car.customer.add(request.user)
        car.quantity -= 1
        car.save() 

        messages.success(request, f"Order for '{car.title}' placed successfully!")
        return redirect('home')
    else:
        messages.warning(request, "Please log in to continue!")
        return redirect('login')



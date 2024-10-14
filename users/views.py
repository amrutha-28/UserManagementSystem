# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages


# List Users
def user_list(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'users/user_list.html', {'users': users})

def home(request):
    return render(request, 'home.html')

# Add User
def add_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        # Create a new user instance and save it
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address
        )
        user.save()
        return redirect('users:user_list')
    return render(request, 'users/add_user.html')

# Edit User
def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User details updated successfully!')
            return redirect('users:user_list')  # Redirect to the user list after updating
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserForm(instance=user)

    return render(request, 'users/edit_user.html', {'form': form, 'user': user})

# Delete User
def delete_user(request, id):
    user = get_object_or_404(User, id=id)  # This raises a 404 if the user doesn't exist
    if request.method == 'POST':
        user.delete()
        messages.success(request, f'User {user.first_name} {user.last_name} was deleted successfully.')  # Add success message
        return redirect('users:user_list')  # Redirect after deletion
    return render(request, 'users/delete_user.html', {'user': user})
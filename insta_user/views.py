from django.shortcuts import render
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar
from insta_user.forms import EditProfileForm
from django.http import HttpResponseForbidden
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    data = InstaUser.objects.all()
    return render(request, "index.html", {'data': data})

def profile_view(request, username):
    context_dict = {}
    user = InstaUser.objects.get(username=username)
    profile_info = InstaUser.objects.filter(username=user).first()
    users_uploads = FavoriteCar.objects.filter(poster=user.id).all()
    context_dict['info'] = profile_info
    context_dict['my_uploads'] = users_uploads
    return render(request, "user_detail.html", context_dict)

def profile_edit_view(request, username):
    edit = get_object_or_404(InstaUser, username=username)
    if edit.username == request.user.username:
        if request.method == "POST":
            form = EditProfileForm(request.POST, request.FILES, instance=edit)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.save()
                return redirect('profile', username)
        else:
            form = EditProfileForm(instance=edit)
        return render(request, 'generic_form.html', {'form': form})
    else: return HttpResponseForbidden("You do not have permission to edit this post")
                
    form = EditProfileForm()
    return render(request, 'generic_form.html', {'form': form} )

def del_user(request, username):    
    u = InstaUser.objects.get(username=username)
    u.delete()
    messages.success(request, "The user is deleted")
    return render(request, 'index.html')

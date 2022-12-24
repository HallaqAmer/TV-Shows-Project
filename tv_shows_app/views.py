from django.shortcuts import render,redirect
from django.contrib import messages
from . import models
from .models import Show

#this root route to redirect to shows page
def root(request):
    return redirect("/shows")

# this route displays all the shows
def display_shows(request):
    context={
        "shows": models.get_all_shows()
    }
    return render(request,"shows.html",context)

#this route display a form to add a new show
def new_show(request):
    return render(request,"add_show.html")

def delete_show(request):
    if request.method=="POST":
        showid = request.POST["showid"]
        models.delete_show(showid)
    return redirect("/shows")

#this route creat a new show
def create_new_show(request):
    errors=Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        new_show=models.create_show(request.POST)
        return redirect("/shows/"+str(new_show.id))

#this route display info of a specific show
def display_show_info(request,showid):
    this_show=models.get_show(showid)
    context= {
        "show": this_show
    }
    return render(request,"show_info.html",context)

# this route display the show page for edit
def display_show_edit(request,showid):

    show=models.get_show(showid)
    
    context = {
        "show": show
    }
    return render(request,"edit_show.html",context)

# this route update the show info
def update_show(request,showid):

    errors=Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/edit/"+str(showid))
    else:

    # if request.method=="POST":
        show=models.update_show(request.POST,showid)
        context= {
        "show": show
        }
        return render(request,"show_info.html",context)


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.


def home(request):
    allmovies = Movie.objects.all()#selct * from movie table
    context = {
    'movies':allmovies
    }
    
    return render(request, 'main/index.html',context)
    
 #ditail view   
def ditail(request,id):
    movie = Movie.objects.get(id=id)# Select everything(*) from the database with this id=id
    context = { 'movie': movie }
    return render(request, 'main/ditail.html',context)
    
#Add movies to database
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST or None) 
        
        
       #check if form is valid or not 
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('main:home')
    else:
        form = MovieForm()
    return render(request, 'main/addmovies.html', {'form':form,
                                                    'controller':"Add movies"})
    

#Edit movie
def edit_movies(request,id):
        #get the movie with the id
        movie = Movie.objects.get(id=id)
        
        #form check
        if request.method == "POST":
            form = MovieForm(request.POST or None,instance=movie)
            #check if form is valid
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect('main:ditail', id)
            
        else:
            form = MovieForm(instance=movie)
        return render(request, 'main/addmovies.html',{'form':form, 'controller':"Edit Movies"})
        
 #delete movie post    
def delete_movie(request,id):
    movie = Movie.objects.get(id=id)
    
    #delete the movie -object
    movie.delete()
    return redirect('main:home')
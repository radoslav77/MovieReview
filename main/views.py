from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg

# Create your views here.


def home(request):
    query = request.GET.get("title")
    allmovies = None
    if query:
        allmovies = Movie.objects.filter("title=query")
    else:
        allmovies = Movie.objects.all()#selct * from movie table
    context = {
    'movies':allmovies
    }
    
    return render(request, 'main/index.html',context)
    
 #ditail view   
def ditail(request,id):
    movie = Movie.objects.get(id=id)# Select everything(*) from the database with this id=id
    review = Review.objects.filter(movie=id).order_by("-comment")
    
    score = review.aggregate(Avg("raiting"))['raiting__avg']
    if score == None:
        score = 0
    context = { 'movie': movie,'reviews':review, 'averidge':score }
    return render(request, 'main/ditail.html',context)
    
#Add movies to database
def add_movie(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
        
    
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
        #if they are not admin
        else:
            return redirect('main:home')
            
    #if they are n login 
    return redirect('accounts:login_user')

#Edit movie
def edit_movies(request,id):
        if request.user.is_authenticated:
            if request.user.is_superuser:
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
                #if they are not admin
            else:
                return redirect('main:home')
                
        #if they are n login 
        return redirect('accounts:login_user')
        
        
 #delete movie post    
def delete_movie(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:


            movie = Movie.objects.get(id=id)
                
                #delete the movie -object
            movie.delete()
            return redirect('main:home')
    
    
    
            #if they are not admin
        else:
            return redirect('main:home')
            
    #if they are n login 
    return redirect('accounts:login_user')
    
  #addig review to a movie  
def add_review(request,id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)
        
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST['comment']
                data.raiting = request.POST['raiting']
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect('main:ditail', id)
 
        else:
            form = ReviewForm()
        return render(request, 'main/ditail.html',{'form':form})
        
    else:
        return redirect('accounts:login_user')
     
     #eding a review of a movie   
def edit_review(request,movie_id,review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        #review is after the movie 
        review = Review.objects.get(movie=movie, id=review_id)
        
        #check if the review is done by the looged in user
        if request.user == review.user:
            # grand permission to edit reiew 
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.raiting > 10) or (data.raiting < 0):
                        error = "Out of range.Please select raiting from 0 to 10"
                        return render(request, 'main/editreview.html',{'error':error, 'form':form})
                        
                    else: 
                        data.save()
                        return redirect('main:ditail', movie_id)
                    
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editreview.html',{'form':form})
            # if user is not the autor of the review
        else:
            return redirect('main:ditail', movie_id)
         #if user not logged in   
    else:
        return redirect('main:login')
        
        
#delit review
def delete_review(request,movie_id,review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        #review is after the movie 
        review = Review.objects.get(movie=movie, id=review_id)
        
        #check if the review is done by the looged in user
        if request.user == review.user:
            # grand permissin delete
            review.delete()
        
        return redirect('main:ditail', movie_id)
         #if user not logged in   
    else:
        return redirect('main:login')
    

        
    
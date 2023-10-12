from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView

# Create your views here.

# Class based views 
# Base View
'''class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request,"reviews/review.html",{
            # "has_error": True
            "form": form 
        })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
            "form": form
        })'''
# FormView
'''class ReviewView(FormView):
    form_class = ReviewForm # for rendering and validating
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)'''
# CreateView
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html" 
    success_url = "/thank-you"
    

#Using base view
'''class ThankYouView(View): 
    def get(self, request):
        return render(request, "reviews/thank_you.html")

def thank_you(request):
    return render(request, "reviews/thank_you.html")'''
# Using TemplateView
class ThankYouView(TemplateView):  #Format of TemplateView which render a template and display it as a web page
    template_name = "reviews/thank_you.html" # tell Django which template to render.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


# TemplateView for fetching the data
'''class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context'''
# ListView for Fetching the list of data 
class ReviewsListView(ListView):  
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews" # Custom names
    
    '''def get_queryset(self) : # Allows us to change how the data is fetched
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data'''


# TemplateView for fetching single data
'''class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        # reviews = Review.objects.all()
        context["review"] = selected_review
        return context'''
# DetailView for fetching single data
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review








# Functions based Views
"""
def review(request):
    if request.method == 'POST' :
        # entered_username = request.POST['username'] manually extract data
        form = ReviewForm(request.POST, instance=existing_model)

        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            '''review = Review(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'], 
                rating=form.cleaned_data['rating'])
            review.save()'''
            return HttpResponseRedirect("/thank-you")  
    else:
        form = ReviewForm() # Get request
    
    return render(request,"reviews/review.html",{
        # "has_error": True
        "form": form 
    })
"""       


'''if entered_username =="":
            return render(request,"reviews/review.html",{
                "has_error": True
            })
        print(entered_username)'''
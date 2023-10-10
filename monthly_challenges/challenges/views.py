from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string # useful when we want to generate HTML or text content from a Django template and use it in places where we need a string

# Create your views here.

''' 
#1. Adding multiple views 
def january(request):
    return HttpResponse("Eat no meat for the entire month!")

def february(request):
    return HttpResponse("Walk for atleast 20 minutes every day!")

def march(request):
    return HttpResponse("Learn Django for at least 20 minutes every day!")
'''

'''
#2. Dynamic Path Segments and Captured values
def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for atleast 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)'''



'''
# Path Converters
def challenge_by_number(request, month): 
    return HttpResponse(month)
'''

'''
#Practicing URLs, Views & Dynamic View Logic 
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# Redirects
def challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_url = reverse("monthly_challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_url)
    #return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #response_data = f"<h1>{}</h1>"
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month # Or month.capitalize()
        }) # Short way for below two lines and variable interpolation
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        # return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
'''
# Above upto The Django Visual Studio Code Extension in section 4 

#3. Adding more dynamic View logic
monthly_challenges={
    "january" : "Eat no meat for the entire month!",
    "february" : "Walk for atleast 20 minutes every day!",
    "march" : "Learn Django for at least 20 minutes every day!",
    "april" : "Eat no meat for the entire month!",
    "may" : "Walk for atleast 20 minutes every day!",
    "june" : "Learn Django for at least 20 minutes every day!",
    "july" : "Eat no meat for the entire month!",
    "august" : "Walk for atleast 20 minutes every day!",
    "september" : "Learn Django for at least 20 minutes every day!",
    "october" : "Eat no meat for the entire month!",
    "november" : "Walk for atleast 20 minutes every day!",
    "december" : None,
}

# from Tags and for 
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })

def challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_url = reverse("monthly_challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_url)
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month 
        })
    except:
        raise Http404() # Short way for errors instead of below lines 
        #response_data = render_to_string("404.html")
        #return HttpResponseNotFound(response_data)
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")


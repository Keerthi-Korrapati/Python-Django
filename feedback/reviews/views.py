from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View


# Create your views here.

# Class based views 
class ReviewView(View):
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
        })


def thank_you(request):
    return render(request, "reviews/thank_you.html")

"""
# Functions based Views
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
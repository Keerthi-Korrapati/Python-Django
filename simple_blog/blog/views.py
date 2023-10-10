from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

#Adding dummy data to views file
all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image" : "mountains.jpg",
        "author" : "Keerthi",
        "date" : date(2022, 10, 7),
        "title" : "Mountain Hiking",
        "excerpt" : "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened while I was enjoying the view!",
        "content" : """
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?

            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?
        """
    },
    {
        "slug" : "programming-is-fun",
        "image" : "coding.jpg",
        "author" : "Keerthi",
        "date" : date(2023, 4, 7),
        "title" : "Programming Is Great!",
        "excerpt" : "Did u ever spend hrs searching that one error in your code?",
        "content" : """
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?

            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?
        """
    },
    {
        "slug" : "into-the-woods",
        "image" : "woods.jpg",
        "author" : "Keerthi",
        "date" : date(2021, 5, 27),
        "title" : "Nature at its best",
        "excerpt" : "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content" : """
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?

            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Architecto pariatur animi ratione, molestiae nostrum consequuntur 
            autem ipsum tempore esse minima itaque quia obcaecati cupiditate corporis, 
            reiciendis ab quos quam laboriosam?
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date) # sorted()---> returns a new sorted list , leaving the original list unchanged
    # sorted_posts = all_posts.sort(key=get_date) sort()--> modifies the original list  # Getting free latest posts by filtering
    latest_posts = sorted_posts[-3:] # To access last three elements
    return render(request, "blog/index.html",{
        "posts" : latest_posts
    })
    #pass

def posts(request):
    return render(request,"blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug) # Generator Expression to find next post in a list of posts
    return render(request, "blog/post-detail.html",{
        "post": identified_post
    })


''' slug --> URL-friendly version, 
             typically generated by removing spaces, 
             special characters, and 
             converting letters to lowercase.
            ex :Post Title: "How to Start a Blog"
                Slug: "how-to-start-a-blog"
            You can use this 'slug' to construct the URL for the individual blog post, 
            making it more readable and SEO-friendly
            https://example.com/blog/how-to-start-a-blog.
    next() --> next() function is used to retrieve the next item from the generator that satisfies the condition
'''
import csv
from turtle import title
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from .forms import ContactForm

    # TODO: Define form fields here


from .models import Blog
# Create your views here.

def home(request):
    today = datetime.now()

    search_post = request.GET.get("search")
    if search_post:
        posts = Blog.objects.filter(Q(title__contains=search_post)|Q(post__icontains=search_post))

    else:
        posts = Blog.objects.all()


    return render(request, "blogapp/home.html", {'today': today,
                                                'posts':posts})

def about(request):

    return render(request, "blogapp/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/thanks')
            return redirect('/') #homepage
    else:
        form = ContactForm()

    return render(request, "blogapp/contact.html", {'form':form})

def all_test(request):

    return render(request, "blogapp/all_test.html")

def query_data(request):
    today = datetime.now()

    posts = Blog.objects.all()
    single_row = Blog.objects.get(pk = 3)
    rows = Blog.objects.all()[1:3]
    reversed_posts = Blog.objects.order_by('-id')
    columns = Blog.objects.values('title', 'id')
    first_row = Blog.objects.first()
    last_row = Blog.objects.last()


    return render(request, "blogapp/query_data.html", {'today': today, 
                                                'posts' : posts, 
                                                'single_row': single_row,
                                                'rows': rows,
                                                'reversed_posts' : reversed_posts,
                                                'columns': columns,
                                                'first_row': first_row,
                                                'last_row': last_row
                                                })

def post_details(request, id):
    today = datetime.now()
    single_row = Blog.objects.get(pk=id)
    return render(request, "blogapp/post_details.html", {'single_row':single_row, 'today':today})

def table(request):
    table_obj = Blog.objects.all()
    return render(request, "blogapp/table.html", {'table_obj':table_obj})


def export_csv (request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Deposition'] = 'attachment; fliename="blog.csv"'
    writer = csv.writer(response)

    writer.writerow(['Post','Created Date','Updated Date'])

    post_obj = Blog.objects.all().values_list('title','date_created','date_updated')
    for r in post_obj:
        writer.writerow(r)
    return response

def thanks(requsets):
    return HttpResponse("Thank you")
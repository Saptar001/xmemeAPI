from django.shortcuts import render
from django.http import HttpResponse
from .models import Meme
from . import views
from django.shortcuts import render, redirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]

def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):
    # http://stackoverflow.com/a/10543969/396300
    return any([url.endswith(e) for e in extension_list])

# Create your views here.
def index(request):
    dests=Meme.objects.all() #connecting the database with index.html "the opening page"
    return render(request,"index.html",{'dests':dests})

def add_data_form_submission(request):
    print("Form submitted")
    O_name=request.POST["O_name"]
    O_caption=request.POST["O_caption"]
    url=request.POST["url"]
    # print(len(O_name))
    if len(O_name)>100 or len(O_caption)>200 or len(url)>200:
        return HttpResponse("Characters Limit Exceeded")

    url_validate = URLValidator()
    error="<html><body><h1>Invalid URL</h1></body></html>"
    try:
        url_validate(url)
        print("Correct url")
    except:
        print("Incorrect url")
        return HttpResponse(error)

    res=valid_url_extension(url,VALID_IMAGE_EXTENSIONS)
    inval="<html><body><h1>Please copy correct Image Address</h1></body></html>"
    if res==True:
        print(res)
    else:
        return HttpResponse(inval)

    

    

    html="<html><body><h1>409</h1></body></html>"

    for instance in Meme.objects.all():
        if (instance.name==O_name) and (instance.meme_caption==O_caption) and (instance.meme_url==url):
            return HttpResponse(html)


    meme=Meme(name=O_name,meme_caption=O_caption,meme_url=url)

    meme.save()

    return redirect(index)
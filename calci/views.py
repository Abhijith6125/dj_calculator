from django.shortcuts import render

# Create your views here.
def calci(request):
    my_dict={'insert_me':'i am a text from registration/view.py'}
    return render(request,'style.html')
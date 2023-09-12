from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Clara',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.

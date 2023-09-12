from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Clara',
        'class': 'math',
        'slot available': '15',
        'description': 'math class available for 15 person'

    }

    return render(request, "main.html", context)
# Create your views here.

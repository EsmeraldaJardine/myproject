from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': 'The Students and their cats are:'}
    return render(request, 'pets_for_students/index.html', context=context_dict)

def cats(request):
    context_dict = {'boldmessage': 'All the cats are:'}
    return render(request, 'pets_for_students/cats.html', context=context_dict)





from django.shortcuts import render
from pets_for_students.models import Student, Cat


def index(request):
    student_list = Student.objects.order_by('last_name')
    cats_list = Cat.objects.order_by('name')
    #cat_list = Cat.objects.order_by('num_of_cats') order by???
    context_dict = {}
    context_dict['boldmessage'] = 'The Students and their cats are:'
    context_dict['students'] = student_list
    context_dict['pet_list'] = cats_list
    return render(request, 'pets_for_students/index.html', context=context_dict)


def cats(request):
    cats_list = Cat.objects.order_by('name')
    context_dict = {}
    context_dict['boldmessage'] = 'All the cats are:'
    context_dict['cats'] = cats_list
    return render(request, 'pets_for_students/cats.html', context=context_dict)





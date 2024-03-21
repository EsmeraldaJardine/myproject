from django.shortcuts import render
from pets_for_students.models import Student, Cat


def index(request):
    student_list = Student.objects.order_by('last_name')
    for student in student_list:
        num_of_cats = Cat.objects.filter(owner=student).count()
        student.num_of_cats = num_of_cats

    cats_list = Cat.objects.order_by('name')
    context_dict = {}
    context_dict['boldmessage'] = 'The Students and their cats are:'
    context_dict['students'] = student_list
    context_dict['pet_list'] = cats_list
    return render(request, 'pets_for_students/index.html', context=context_dict)


def pets(request):
    cats_list = Cat.objects.order_by('name')
    context_dict = {}
    context_dict['boldmessage'] = 'All the cats are:'
    context_dict['cats'] = cats_list
    return render(request, 'pets_for_students/pets.html', context=context_dict)





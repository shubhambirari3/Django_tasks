from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
   

def template_sample(request):
    return render(request, 'index.html') 

def proj_template(request):
    return render(request, 'proj_index.html')

students = {
    'student_1': {
        'name': 'shubham',
        'age': 20,
        'grade': 'A'
    },
    'student_2': {
        'name': 'ram',
        'age': 21,
        'grade': 'B'
    },  
    'student_3': {
        'name': 'sham',
        'age': 22,
        'grade': 'C'
    }
}

def student_template(request):
    
    return render(request, 'students.html', {'students': students})

def student_name(request):
    names = ["shubbham", "ram", "sham" ]
    return render(request, 'studentName.html', {'name': names})



    



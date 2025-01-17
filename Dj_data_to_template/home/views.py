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

data = {
    'title': 'Employee Details',
    'employees': [
        {'id': 1, 'name': 'Shubham', 'department': 'IT', 'salary': 60000},
        {'id': 2, 'name': 'ram', 'department': 'HR', 'salary': 45000},
        {'id': 3, 'name': 'sham', 'department': 'Finance', 'salary': 50000},
    ]
}

def employee_details(request):
    return render(request, 'emp_details.html', {'data': data})




    



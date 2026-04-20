from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from college_app.models import Department,Students,Teachers
from college_app.forms import StudentForm,TeacherForm,DepartmentForm

def home(a):
        return render(a, 'home.html')


def reg(a):
    message=""
    if a.method=='POST':
        user_name=a.POST.get('username')
        email=a.POST.get('useremail')
        p1=a.POST.get('password1')
        p2=a.POST.get('confirm')
        if p1!=p2:
            message="password not matches"
            return render(a,'register.html',{'message':message})
        elif User.objects.filter(email=email).exists():
            message='email exists...'
            return render(a,'register.html',{'message':message})
        else:
            user=User.objects.create_user(username=user_name,email=email,password=p1)
            user.save()
            return redirect('LOG1')
    return render(a,'register.html')
def login1(a):
    message=""
    if a.method=='POST':
       l_user_name=a.POST.get('username')
       l_p1=a.POST.get('password1')
       user=authenticate(a,username=l_user_name,password=l_p1)
       if user is not None:
          login(a,user)
          return redirect('HOME')
       else:
             message="invalid details"
    return render(a,'login.html',{'message':message})











class department(View):
    def get(self,request):
        data=Department.objects.all()
        context={
            'data':data
        }
        return render(request,'dep.html',context)
class department_create(View):
    def get(self, request):
        form = DepartmentForm()
        return render(request, 'depform.html', {'form': form})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dep')
        return render(request, 'depform.html', {'form': form})     
    
class department_delete(View):
    def get(self, request, id):
        return render(request, 'delform.html', {'id': id})

    def post(self, request, id):
        username = request.POST.get('username')
        password = request.POST.get('password')


        if username == "Teja" and password == "Teja@2004":
            data = Department.objects.get(id=id)
            data.delete()
            return redirect('Dep')
        else:
            message = "Invalid details"
            return render(request, 'delform.html', {
                'message': message,
                'id': id
            })








class teacher(View):
    def get(self,a):
        data=Teachers.objects.all()
       
        context={
            'data':data,
            
        }
        return render(a,'teach.html',context)
class teacher_create(View):
    def get(self, request):
        form1 = TeacherForm()
        return render(request, 'teachform.html', {'form1': form1})

    def post(self, request):
        form1 = TeacherForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('TEACH')
        return render(request, 'teachform.html', {'form1': form1})
class teacher_update(View):
    def get(self,a,id):
        data=Teachers.objects.get(id=id)
        form1=TeacherForm(instance=data)
        context={'form1':form1}
                 
        return render(a,'teachform.html',context)
    def post(self,a,id):
        data=Teachers.objects.get(id=id)
        if a.method=='POST':
            form1=TeacherForm(a.POST,instance=data)
            if form1.is_valid():
                form1.save()
                return redirect('TEACH')
        context={'form1':form1}
        return render (a,'teachform.html',context)
class teacher_delete(View):
    def get(self, request, id):
        return render(request, 'delform.html', {'id': id})

    def post(self, request, id):
        username = request.POST.get('username')
        password = request.POST.get('password')


        if username == "Teja" and password == "Teja@2004":
            data =Teachers.objects.get(id=id)
            data.delete()
            return redirect('TEACH')
        else:
            message = "Invalid details"
            return render(request, 'delform.html', {
                'message': message,
                'id': id
            })








class student(View):
    def get(self,a):
        data=Students.objects.all()
       
        context={
            'data':data,
           
        }
        return render(a,'std.html',context)
class student_create(View):
    def get(self, request):
        form2 = StudentForm()
        return render(request, 'stdform.html', {'form2': form2})

    def post(self, request):
        form2 = StudentForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('STU')
        return render(request, 'stdform.html', {'form2': form2})
class student_update(View):
    def get(self,a,id):
        data=Students.objects.get(id=id)
        form2=StudentForm(instance=data)
        context={'form2':form2}
                 
        return render(a,'stdform.html',context)
    def post(self,a,id):
        data=Students.objects.get(id=id)
        if a.method=='POST':
            form2=StudentForm(a.POST,instance=data)
            if form2.is_valid():
                form2.save()
                return redirect('STU')
        context={'form2':form2}
        return render (a,'stdform.html',context)
class student_delete(View):
    def get(self, request, id):
        return render(request, 'delform.html', {'id': id})

    def post(self, request, id):
        username = request.POST.get('username')
        password = request.POST.get('password')


        if username == "Teja" and password == "Teja@2004":
            data =Students.objects.get(id=id)
            data.delete()
            return redirect('STU')
        else:
            message = "Invalid details"
            return render(request, 'delform.html', {
                'message': message,
                'id': id
            })

            


  

# Create your views here.

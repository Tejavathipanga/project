from django.urls import path
from college_app.views import department,teacher,teacher_update,teacher_delete,student,student_update,student_delete,reg,login1,home,department_delete,department_create,student_create,teacher_create
urlpatterns = [
    
   path("",reg,name='reg1'),
   path("log/",login1,name='LOG1'),
   path("home1/",home,name='HOME'),
   path("create/",student_create.as_view(),name="STU1"),
   path("create1/",department_create.as_view(),name='Dep1'),
   path("create2/",teacher_create.as_view(),name="TEACH1"),
   path("del3<int:id>/",department_delete.as_view(),name='delete2'),
   path("dep/",department.as_view(),name='Dep'),
   path("Teach/",teacher.as_view(),name='TEACH'),
   path("up/<int:id>/",teacher_update.as_view(),name='update'),
   path("del/<int:id>/",teacher_delete.as_view(),name='delete'),
   path("stdu/",student.as_view(),name='STU'),
   path("up1/<int:id>/",student_update.as_view(),name='update1'),
   path("del1/<int:id>/",student_delete.as_view(),name='delete1')
]

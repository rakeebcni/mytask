from django.shortcuts import render, redirect
from myapp.models import*
from myapp.forms import*




def adjob(request):

    if request.method=='POST':


        form=adjobform(request.POST)

        if form.is_valid():

            form.save()

            return redirect('viewJob')

    return render (request, 'job.html', {'form':form})

def viewJob(request):

    viewJob=AddJobTable.objects.all()

    form=adjobform()
   
    context={

        'viewJobs':viewJob,
        'forms':form
    
    }


    return render (request, 'job.html', context)



def deleteJob (request, myid):

    job=AddJobTable.objects.get(id=myid)

    job.delete()
    
    return redirect('viewJob')


def editjob(request,myid):
    
    job=AddJobTable.objects.get(id=myid)

    form=adjobform(instance=job)

    if request.method=='POST':
        
        form=adjobform(request.POST, instance=job )
        
        form.save()

        return redirect('viewJob')


    return render(request, 'editjob.html', {'form':form})


def AddStudent (request):

    student=StudentTable.objects.all()

    if request.method=='POST':
        form=StudentInput(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('AddStudent')
        

    else:
        form=StudentInput()


        context={

        'students':student,
        'form':form
    }

    return render(request, 'AddStudent.html', context)


def AddMarks(request):

    StudentMarks=MarksTable.objects.all()

    CGPA=None
    Grade=None


    if request.method=='POST':
        form=MarksInput(request.POST)
        
        if form.is_valid():
            Marks=form.cleaned_data['Marks']
           
            if Marks>=80:
                CGPA,Grade=4,'A+'
            elif Marks<=80 and Marks>=70:
                CGPA=3
            
            elif Marks<=70 and Marks >=60:
                CGPA, Grade=2, 'A'

            elif Marks<=70:
                CGPA, Grade=1,'B+'
            else:
                CGPA,Grade=0,'B'
    
            mark=form.save()
            mark.CGPA=CGPA
            mark.Grade=Grade
            mark.save()
            return redirect('AddMarks')
        
    else:
        form=MarksInput()

    context={
        'marks':StudentMarks,
        'form': form
    }

    return render(request, 'Addmarks.html', context)


def AddGrade (request):

    if request.method=='POST':
        form=GradeInput(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('AddGrade')
        

    else:
        form=GradeInput()

    return render(request, 'Addgrade.html', {'form':form})



def NavbarPage(request):

    
    return render(request, "navbar.html")



def addCourse (request):

    course=CourseTable.objects.all()

    if request.method=='POST':
        form=CourseInput(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('addCourse')
    else:
        form=CourseInput()
        
    
    context={

        'courses':course,
        'form':form
    }


    return render(request, 'adcourse.html', context)


def DeleteStudent(request, myid):

    student=StudentTable.objects.get(id=myid)

    student.delete()

    return redirect('AddStudent')


def DeleteMarks(request, myid):

    marks=MarksTable.objects.get(id=myid)

    marks.delete()

    return redirect('AddMarks')

    
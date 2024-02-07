from django.db import models

# Create your models here.

class AddJobTable(models.Model):

    myJob_Title=models.CharField(max_length=100)
    Company_Name=models.CharField(max_length=100)
    Company_Description=models.CharField(max_length=100)
    Qualifications=models.CharField(max_length=100)
    Location_Name=models.CharField(max_length=100)
    Job_Description=models.CharField(max_length=100)
    Application_Deadline=models.DateTimeField(max_length=100)

    def __str__(self) -> str:
        return self.myJob_Title


class CourseTable(models.Model):

    Course_Name=models.CharField(max_length=100,null=True)
    Credit_Hour=models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.Course_Name



class StudentTable(models.Model):

    gender=[
        ('male','Male'), ('female','Female')

    ]

    Student_Name=models.CharField(max_length=100, null=True)
    Student_Age=models.IntegerField(null=True)
    Gender=models.CharField( choices=gender, max_length=100, null=True)
    Student_Department=models.CharField(max_length=100,null=True)
    Courses=models.ManyToManyField(CourseTable)
    

    
    def __str__(self) -> str:
        return self.Student_Name


class MarksTable(models.Model):

    Student_Name=models.ForeignKey(StudentTable, on_delete=models.CASCADE, null=True )
    Course_Name=models.ForeignKey(CourseTable, related_name = 'Course_Name', on_delete=models.CASCADE, null=True )
    Marks=models.IntegerField(null=True)
    CGPA=models.FloatField(null=True)
    Grade=models.CharField(null=True, max_length=100 )
    credit=models.ForeignKey(CourseTable, related_name = 'Credit_Hour', on_delete=models.CASCADE,null=True )
    
    # def __str__(self) -> str:
    #     return self.Student_Name.Student_Department

class GradeTable(models.Model):

    Student_Name=models.ForeignKey(StudentTable, on_delete=models.CASCADE, null=True )
    Grade_sum=models.FloatField(null=True, blank=True)



    
    # def save(self, *args, **kwargs):
    #     self.Grade_sum= MarksTable.objects.filter(Student_Name_id=1).aggregate(sum(float('CGPA')))['CGPA__sum']
    
    
    
    # def __str__(self):

    #     return self.Student_Name.Student_Name


    
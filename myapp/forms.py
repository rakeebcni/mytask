from django import forms
from myapp.models import*


class adjobform(forms.ModelForm):

    class Meta:
        model=AddJobTable
        fields= ['myJob_Title','Company_Name', 'Company_Description', 'Qualifications', 'Location_Name', 'Job_Description', 'Application_Deadline']
        labels={

            'myJob_Title':'Enter your Job Title',
            'Company_Name':'Enter your Company Name',
            'Company_Description' : 'Enter your Company Description',
            'Qualifications':'Enter your Qualifications',
            'Location_Name':'Enter your Location Name',
            'Job_Description':'Enter your Job Description',
            'Application_Deadline':'Enter your Application Deadline',

        }
        widgets= {
            'Application_Deadline':forms.DateTimeInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            ),

            'Company_Description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'Job_Description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

        
class CourseInput(forms.ModelForm):

    class Meta:
        model=CourseTable
        fields= ['Course_Name','Credit_Hour']
        labels={

            'Course_Name':'Enter your Course Name',
            'Credit_Hour':'Enter Credit Hour',


        }
        
class StudentInput(forms.ModelForm):

    class Meta:
        model=StudentTable
        fields= ['Student_Name','Student_Department', 'Gender', 'Student_Age', 'Courses']
        labels={

            'Student_Name':'Enter Student Name',
            'Student_Department':'Enter Student Department',
            'Gender':'Enter Your Gender',
            'Student_Age':'Enter Your Age',
            'Courses':'Enter Course Name',


        }

class MarksInput(forms.ModelForm):

    class Meta:
        model=MarksTable
        fields= ['Student_Name','Course_Name','Marks',]
        labels={

            'Student_Name':'Enter Student Name',
            'Course_Name':'Enter Course Name',
            'Marks':'Enter Marks',
        }

class GradeInput(forms.ModelForm):

    class Meta:
        model=GradeTable
        fields= ['Student_Name']
        labels={

            'Student_Name':'Enter Student Name',
            
        }
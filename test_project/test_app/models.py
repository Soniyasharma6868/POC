from django.db import models




class Student(models.Model):
    Name = models.CharField(max_length=100)
    College_name = models.CharField(max_length=100)
    Year = models.CharField(max_length=100)


    class Meta:
        db_table = "Student"

class Teachers(models.Model):
    Name = models.CharField(max_length=100)
    Deparment = models.CharField(max_length=100)
    Year = models.CharField(max_length=100)

class Books(models.Model):
    Student = models.ForeignKey(Student,on_delete=models.CASCADE, blank=True, null=True,related_name='book')
    teachers = models.ForeignKey(Teachers, on_delete=models.CASCADE, blank=True, null=True,related_name='book')
    Book_name = models.CharField(max_length=100)



    class Meta:
        db_table = "Books"

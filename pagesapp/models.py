from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    ball = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    # def sort(self): 
    #     sortedData = [] 
    #     for i in self: 
    #         if i['ball'] >= 30: 
    #             sortedData.append(i)
    #             sortedData.sort(key=lambda k: k['ball'], reverse=True) 
    #             print(sortedData[:5])
    #     return sortedData[:5]
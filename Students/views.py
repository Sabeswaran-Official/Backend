# from django.shortcuts import render

# Create your views here.


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from decouple import config


class StudentAPI(APIView):

   
    # permission_classes=[IsAuthenticated]

    def get(self,request,task_id=None):

        if task_id==None:

            all_students=Student.objects.all()
            student_list=Student_Task_Serializer(all_students,many=True).data

            return Response(student_list)
        
        else:
            a_student=Student.objects.get(task_id=id)
            student=Student_Serializer(a_student).data

            return Response(student)

        # student_list=[]

        # for s in all_students:
        #     stud_dict={
        #         "id":s.id,
        #         "name":s.name,
        #         "age":s.age,
        #         "d_o_b":s.d_o_b,
        #         "place":s.place,
        #         "admin":s.admin
        #     }
        #     student_list.append(stud_dict)
        
        

    def post(self,request):
        print(request.data)

        new_student=Student(name=request.data['name'],age=request.data['age'],d_o_b=request.data['d_o_b'],place=request.data['place'],admin=request.data['admin'])
        new_student.save()

        return Response("New user created")
    
    def put(self,request,stud_id):
        print(f"student_id {stud_id}")

        student_data=Student.objects.filter(id=stud_id)

        print(request.data)

        student_data.update(name=request.data['name'],age=request.data['age'],d_o_b=request.data['d_o_b'],place=request.data['place'],admin=request.data['admin'])

        return Response("Data's has been updated")
    
    def delete(self,request,stud_id):

        student_data=Student.objects.filter(id=stud_id)

        student_data.delete()

        return Response("Student data has been deleted")
    
class TaskAPI(APIView):

    # permission_classes=[IsAuthenticated]

    def get(self,request,task_id=None):

        if task_id==None:

            person_name=config('name')     # for reference for env file/config
            print(person_name)

            all_tasks=Task.objects.all()

            task_data=Task_Data_Serializer(all_tasks ,many=True).data

            return Response(task_data)
        else:
            task=Task.objects.get(id=task_id)
            task_data=Task_Data_Serializer(task).data

            return Response(task_data)


    def post(self,request):
        new_task=Task_Serializer(data=request.data)

        if new_task.is_valid():
            new_task.save()

            return Response("New task added")
        else:

            return Response(new_task.errors)
        
    def patch(self,request,task_id):
        task=Task.objects.get(id=task_id)

        update_task=Task_Serializer(task,data=request.data,partial=True)

        if update_task.is_valid():
            update_task.save()

            return Response("Task updated")
        else:
            return Response(update_task.errors)
        
    def put(self,request,task_id):
        task=Task.objects.get(id=task_id)

        update_task=Task_Serializer(task,data=request.data,partial=True)
        
        if update_task.is_valid():
            update_task.save()

            return Response("Task has updated")
        else:
            return Response(update_task.errors)
        
    def delete(self,request,task_id):
        
        task=Task.objects.get(id=task_id)
        task.delete()

        return Response("Task has deleted")
    
'''# This separate view for api with id  ,now it is no use ,when we use dynamic get method
class TaskAPIById(APIView):

    def get(self,request,task_id):
        task=Task.objects.get(id=task_id)
        task_data=Task_Serializer(task).data

        return Response(task_data)
    
    def patch(self,request,task_id):
        task=Task.objects.get(id=task_id)

        update_task=Task_Serializer(task,data=request.data,partial=True)

        if update_task.is_valid():
            update_task.save()

            return Response("Task updated")
        else:
            return Response(update_task.errors)
        
    def put(self,request,task_id):
        task=Task.objects.get(id=task_id)

        update_task=Task_Serializer(task,data=request.data,partial=True)
        
        if update_task.is_valid():
            update_task.save()

            return Response("Task has updated")
        else:
            return Response(update_task.errors)
        
    def delete(self,request,task_id):
        
        task=Task.objects.get(id=task_id)
        task.delete()

        return Response("Task has deleted")
'''

class RankView(APIView):

    def get(self,request,id=None):
        if id==None:
            all_data=RankSheet.objects.all()
            rank_data=RankSheet_Serializer(all_data ,many=True).data

            return Response(rank_data)
        else:
            data=RankSheet.objects.get(id=id)
            rank_data=RankSheet_Serializer(data).data

            return Response(rank_data)

    def post(self,request):

        total_marks=request.data['tamil']+request.data['english']+request.data['maths']+request.data['science']+request.data['social_science']

        average_marks=total_marks/5

        if (request.data['tamil']>=35) and (request.data['english']>=35) and (request.data['maths']>=35) and (request.data['science']>=35) and (request.data['social_science']>=35):
            student_result=True
        else:
            student_result=False

        new_data=RankSheet(tamil=request.data['tamil'],english=request.data['english'],maths=request.data['maths'],science=request.data['science'],social_science=request.data['social_science'],total=total_marks,average=average_marks,result=student_result)

        new_data.save()

        return Response("Your marks has added")
    
    def patch(self,request,id):

        rank=RankSheet.objects.filter(id=id)

        total_marks=request.data['tamil']+request.data['english']+request.data['maths']+request.data['science']+request.data['social_science']

        average_marks=total_marks/5

        if (request.data['tamil']>=35) and (request.data['english']>=35) and (request.data['maths']>=35) and (request.data['science']>=35) and (request.data['social_science']>=35):
            student_result=True
        else:
            student_result=False

        rank.update(tamil=request.data['tamil'],english=request.data['english'],maths=request.data['maths'],science=request.data['science'],social_science=request.data['social_science'],total=total_marks,average=average_marks,result=student_result)

        return Response("Marks has updated")
    
    def put(self,request,id):

        rank=RankSheet.objects.filter(id=id)

        total_marks=request.data['tamil']+request.data['english']+request.data['maths']+request.data['science']+request.data['social_science']

        average_marks=total_marks/5

        if (request.data['tamil']>=35) and (request.data['english']>=35) and (request.data['maths']>=35) and (request.data['science']>=35) and (request.data['social_science']>=35):
            student_result=True
        else:
            student_result=False

        rank.update(tamil=request.data['tamil'],english=request.data['english'],maths=request.data['maths'],science=request.data['science'],social_science=request.data['social_science'],total=total_marks,average=average_marks,result=student_result)

        return Response("Marks has updated")
    
    def delete(self,request,id):
        data=RankSheet.objects.get(id=id)

        data.delete()

        return Response("Marks has deleted")
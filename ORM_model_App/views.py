from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Teacher, Management, ITDepartment, BBIT
from .serializer import StudentSerializer, ManagementSerializer, TeacherSerializer, ITDepartmentSerializer, \
    BBITSerializer


#GET Student
@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)



#Student
@api_view(['POST'])
def student_create(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        student.delete()
        return JsonResponse({"message": "Student deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def student_update(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


# Teacher
@api_view(['POST'])
def teacher_create(request):
    if request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def teacher_delete(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Teacher Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        teacher.delete()
        return JsonResponse({"message": "Teacher deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def teacher_update(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#management

@api_view(['GET'])
def management_list(request):
    if request.method == 'GET':
        management = Management.objects.all()
        serializer = ManagementSerializer(management, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def management_create(request):
    if request.method == 'POST':
        serializer = ManagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def management_delete(request, pk):
    try:
        management = Management.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "member Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        management.delete()
        return JsonResponse({"message": "member deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def management_update(request, pk):
    try:
        management = Management.objects.get(pk=pk)
    except Management.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ManagementSerializer(management, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# for IT Department

@api_view(['GET'])
def ITDepartment_list(request):
    if request.method == 'GET':
        itdepartment = ITDepartment.objects.all()
        serializer = ITDepartmentSerializer(itdepartment, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def ITDepartment_create(request):
    if request.method == 'POST':
        serializer = ITDepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def ITDepartment_delete(request, pk):
    try:
        itdepartment = ITDepartment.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "member Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        itdepartment.delete()
        return JsonResponse({"message": "member deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def ITDepartment_update(request, pk):
    try:
        itdepartment = ITDepartment.objects.get(pk=pk)
    except ITDepartment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ITDepartmentSerializer(itdepartment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# for BBIT departemnt

@api_view(['GET'])
def BBIT_list(request):
    if request.method == 'GET':
        Bbitdepartment = BBIT.objects.all()
        serializer = BBITSerializer(Bbitdepartment, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def BBIT_create(request):
    if request.method == 'POST':
        serializer = BBITSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def BBIT_delete(request, pk):
    try:
        Bbitdepartment = BBIT.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "member Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        Bbitdepartment.delete()
        return JsonResponse({"message": "member deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def BBIT_update(request, pk):
    try:
        Bbitdepartment = BBIT.objects.get(pk=pk)
    except BBIT.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BBITSerializer(Bbitdepartment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
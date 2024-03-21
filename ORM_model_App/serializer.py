from .models import Student, Teacher, Management, ITDepartment, BBIT
from rest_framework import serializers



class StudentSerializer(serializers.ModelSerializer):    #used for serializing and deserializing Teacher model instances into JSON format and vice versa
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'enrolment', 'subject', 'email', 'phone_number', 'fk']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        Fields = '__all__'

class BBITSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBIT
        Fields = ['id', 'dep_name', 'students']




class ITDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITDepartment
        Fields = '__all__'



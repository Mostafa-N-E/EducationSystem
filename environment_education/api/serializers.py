from rest_framework import serializers
from environment_education.models import College, Class, Lesson


class CollegeSerializer(serializers.ModelSerializer):
    student_college = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        # view_name='person:s_student_list'
    )

    class Meta:
        model = College
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields = '__all__'

# class StudentSerializer(serializers.ModelSerializer):
#     rented_book = BookSerializer(many=False)
#
#     class Meta:
#         model = Student
#         fields = '__all__'




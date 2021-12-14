from rest_framework import serializers
from persons.models import Professor,Student, ClassLesson
from library.api.serializers import BookSerializer
from environment_education.api.serializers import ClassSerializer, LessonSerializer
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# have_lesson = ClassLesson.objects.filter(students__username=request.user.username).filter(
#         cluss__college__name=stu.college.name)
#     have_not_lesson = ClassLesson.objects.exclude(students__username=request.user.username).filter(
#         cluss__college__name=stu.college.name)


LAESSONS_CHOICES = [ ( classLesson.id, classLesson.lesson ) for classLesson in ClassLesson.objects.all() ]

class SelectClassLessonSerializer(serializers.Serializer):
    student_id = serializers.IntegerField(read_only=True)
    lessons = serializers.ChoiceField(choices=LAESSONS_CHOICES, default='python')
    have_lessons = serializers.CharField()
    have_not_lessons = serializers.SerializerMethodField('have_lessons')

    def create(self, validated_data):
        return ClassLesson.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.student_id = validated_data.get('student_id', instance.student_id)
        instance.lessons = validated_data.get('lessons', instance.lessons)
        instance.save()
        return instance

    def have_lessons(self):


        serializer = LessonSerializer()
        return serializer.data
# c = ClassLesson.objects.get()
# serializer_classLesson = SelectClassLessonSerializer(c)


class StudentSerializer(serializers.ModelSerializer):
    rented_book = BookSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    # professor = serializers.PrimaryKeyRelatedField(      # lesson_professor
    #     many=True,
    #     read_only=True,
    #     # view_name='person:s_student_list'
    # )
    class Meta:
        model=Professor
        fields = '__all__'


class ClassLessonSerializer(serializers.ModelSerializer):
    cluss = ClassSerializer(many=False)
    professor = ProfessorSerializer(many=False)
    students = StudentSerializer(many=True)
    lesson = LessonSerializer(many=False)

    # have_lessons = serializers.CharField()
    have_lessons = serializers.SerializerMethodField('have_lessons')
    class Meta:
        model = ClassLesson
        fields = '__all__'

    def have_lessons(self, obj):

        serializer = LessonSerializer()
        return serializer.data
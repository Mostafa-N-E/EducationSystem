from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from persons.models import Professor,Student, ClassLesson
from .serializers import ProfessorSerializer, StudentSerializer, ClassLessonSerializer,SelectClassLessonSerializer

from rest_framework import generics

class SelectClassLessonAPI( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Student.objects.all()
    serializer_class = SelectClassLessonSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.all()
    #
    def get_object(self,*args, **kwargs):
        queryset = self.queryset
        filter = {'pk':self.request.user.id}
        # for field in self.multiple_lookup_fields:
        #     filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        # self.check_object_permissions(self.request, obj)
        return obj




@api_view(['GET', 'POST'])
def professor_list(request):

    if request.method == 'GET' :
        response = dict()
        response['perofessor'] = ProfessorSerializer(Professor.objects.all(),many=True).data
        return Response(response)

    elif request.method == 'POST' :
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def professor_detail(request,pk):
    try:
        professor = Professor.objects.get(id=pk)
    except:
        return Response(status=404)

    if request.method == 'GET' :
        res = dict()
        res['perofessor'] = ProfessorSerializer(professor,many=True).data
        return Response(res)


#  generics.RetrieveModelMixin, generics.UpdateModelMixin, generics.DestroyModelMixin = generics.RetrieveUpdateDestroyAPIView
class Student_api(generics.CreateModelMixin, generics.RetrieveUpdateDestroyAPIView):
    pass

class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroyApi(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ListStudent_api(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all students.
        """
        if self.request.user.is_superuser:
            # students = ClassLesson.objects.all()
            students = [student for student in ClassLesson.objects.all()]
        else:
            students = ClassLesson.objects.filter(professor__username=self.request.user.username).annotate(Count('students'))

        return Response(students)


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        # response = dict()
        students = StudentSerializer(Student.objects.all(), many=True).data
        return Response(students)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request,pk):
    try:
        student = Student.objects.get(id=pk)
    except:
        return Response(status=404)

    if request.method == 'GET' :
        res = dict()
        res['student'] = ProfessorSerializer(student,many=True).data
        return Response(res)



@api_view(['GET', 'POST'])
def classLesson_list(request):
    if request.method == 'GET':
        # response = dict()
        classLesson = StudentSerializer(ClassLessonSerializer.objects.all(), many=True).data
        return Response(classLesson)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def classLesson_detail(request,pk):
    try:
        classLesson = ClassLesson.objects.get(id=pk)
    except:
        return Response(status=404)

    if request.method == 'GET' :
        res = dict()
        res['classLesson'] = ProfessorSerializer(classLesson,many=True).data
        return Response(res)


from rest_framework import viewsets


class ClassLessonViewSet(viewsets.ViewSet):
    serializer_class = ClassLessonSerializer
    queryset = ClassLesson.objects.all()

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        # serializer = super().get_
        stu = self.request.user
        have_lesson = ClassLesson.objects.filter(students__username=self.request.user.username).filter(cluss__college__name=stu.college.name)
        have_not_lesson = ClassLesson.objects.exclude(students__username=self.request.user.username).filter(cluss__college__name=stu.college.name)
        x = {
            'have_lesson' :have_lesson,
            'have_not_lesson':have_not_lesson
              }
        serializer = ClassLessonSerializer(x, meny=True)

        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
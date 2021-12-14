from rest_framework.decorators import api_view
from rest_framework.response import Response
from environment_education.models import College
from .serializers import CollegeSerializer

@api_view(['GET', 'POST'])
def college_list(request):

    if request.method == 'GET' :
        # response = dict()
        college = CollegeSerializer(College.objects.all(),context={'request':request},many=True).data
        return Response(college)

    elif request.method == 'POST' :
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def college_detail(request,pk):
    try:
        college = College.objects.get(id=pk)
    except:
        return Response(status=404)

    if request.method == 'GET' :
        # res = dict()
        college = CollegeSerializer(college,many=True).data
        return Response(college)

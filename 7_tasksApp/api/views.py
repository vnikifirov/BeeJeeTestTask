from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics, status, viewsets, permissions
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from .serializers import UserSerializer, UserSerializerWithToken

# class UserView(generics.CreateAPIView):
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	# tasks = Task.objects.all().order_by('-id')
	# serializer = TaskSerializer(tasks, many=True)
	# return Response(serializer.data)

	data = []
	nextPage = 1
	previousPage = 1
	task = Task.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(task, 3)
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)

	serializer = TaskSerializer(data,context={'request': request} ,many=True)
	if data.has_next():
		nextPage = data.next_page_number()
	if data.has_previous():
		previousPage = data.previous_page_number()

	return Response({'data': serializer.data ,
		'count': paginator.count,
		'numpages' : paginator.num_pages,
		'nextlink': '/task-list/?page=' + str(nextPage),
		'prevlink': '/task-list/?page=' + str(previousPage)})

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
	
	return Response(serializer.data)

@api_view(['POST'])
@login_required
# @permission_classes([IsAuthenticated])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
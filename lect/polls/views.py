from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import TodoList,TodoItem
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime

# Create your views here.

def index(request):
    list_todo = TodoList.objects.all()
    # template = loader.get_template('polls/index.html')
    context = {
        'todolists':list_todo,
    }
    # list_items = TodoItem.objects.all()
    # output = ', '.join(item.title for item in list_items)
    return render(request, 'polls/index.html' , context)

def detail(request,list_id):
    try:
        todolist=TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This list does not exist")

    items_list=TodoItem.objects.filter(todo_list=todolist)
    context={
        'todolist':todolist,
        'items_list':items_list
    }
    return render(request, 'polls/detail.html',context)

def create(request):

    if request.method == 'GET':
        return render(request, 'polls/createlist.html')

    name = request.POST["name"]

    TodoList.objects.create(list_name=name)
    lists = TodoList.objects.all()
    context = {
        'todolists':lists
    }

    return redirect('../')

def createItem(request,list_id):

    if request.method == 'GET':
        try:
            todolist=TodoList.objects.get(id=list_id)
        except TodoList.DoesNotExist:
            raise Http404("This list does not exist")
        context={
            'todolist':todolist
        }
        return render (request, 'polls/createItem.html',context)
    
    todolist=TodoList.objects.get(id=list_id)
    title = request.POST["title"]
    try:
        check = request.POST["check_box"]
    except MultiValueDictKeyError:
        check = False
    date_time = request.POST["date_time"]
    if(check=='on'):
        check = True
    TodoItem.objects.create(title=title,checked=check,due_date=date_time,todo_list=todolist)
    
    
    items_list=TodoItem.objects.filter(todo_list=todolist)
    context={
        'todolist':todolist,
        'items_list':items_list
    }
    return redirect('../'+str(list_id)+'/')

def deleteList(request,list_id):

    TodoList.objects.filter(id=list_id).delete()
    
    return redirect('../')

def deleteItem(request,list_id,item_id):

    todolist=TodoList.objects.get(id=list_id)
    TodoItem.objects.filter(id=item_id,todo_list=todolist).delete()
    
    return redirect('../')

def update(request,list_id,item_id):

    if request.method == 'GET':
        try:
            todolist=TodoList.objects.get(id=list_id)
        except TodoList.DoesNotExist:
            raise Http404("This list does not exist!!")
        try:

            list_item = TodoItem.objects.get(id=item_id,todo_list=todolist)
        except TodoItem.DoesNotExist:
            raise Http404("This list item does not exist!!")
        check_box=""
        if(list_item.checked==True):
            check_box="checked"
        # date = list_item.due_date.format()
        myDate = list_item.due_date
        formatedDate = myDate.strftime("%Y-%m-%dT%H:%M:%S")
        context={
            'todolist':todolist,
            'list_item':list_item,
            'check_box_value':check_box,
            'date_time_dis':formatedDate
        }
        return render (request, 'polls/updateItem.html',context)
    todolist=TodoList.objects.get(id=list_id)
    title = request.POST["title"]
    try:
        check = request.POST["check_box"]
    except MultiValueDictKeyError:
        check = False
    date_time = request.POST["date_time"]
    if(check=='on'):
        check = True
    
    TodoItem.objects.filter(id=item_id,todo_list=todolist).update(title=title,checked=check,due_date=date_time,todo_list=todolist)
    return redirect('../')
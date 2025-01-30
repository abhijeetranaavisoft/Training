from django.shortcuts import render,redirect
from myapp.models import Room,Message
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request,room):
    username=request.GET.get('username')
    room_details=Room.objects.get(name=room)
    return render(request,'room.html',{
        'username':username,
        'room':room,
        'room_details':room_details
    })
    """ 
    request.GET
request.GET is a QueryDict in Django.
It represents the data sent in the query string of an HTTP GET request.
A query string is the part of the URL after the ? symbol, containing key-value pairs (e.g., ?username=John).
Example:
plaintext
Copy
Edit
URL: /somepage/?username=John
request.GET = {'username': 'John'}
2. .get('username')
.get('username') is a method of the QueryDict object.
It retrieves the value associated with the key 'username'.
Example:
python
Copy
Edit
request.GET.get('username')  # Returns 'John' if username=John in the URL
    """
    

def checkview(request):
    room=request.POST['room_name']
    username=request.POST['username']
    
    if Room.objects.filter(name=room).exists():
       return redirect('/' + room + '/?username=' + username)
    else:
        new_room =Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)
    

def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']

    new_message = Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message Sent Successfully')

def getMessages(request,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

        
    

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Hello World<h1>')
    return render(request, 'index.html', {})

def message_view(request):
    url = 'https://api.telegram.org/bot648414359:AAGhhCZlAe7DTL8tvBUvrFC5vj-TQW-g5fY/sendMessage?chat_id=28713807&text='
    user_name = request.POST.get("name")
    user_email = request.POST.get("email")
    user_message = request.POST.get("message")
    print(user_message)

    return HttpResponseRedirect(url+user_name+'\n'+user_email+'\n'+user_message) #브라우저 창 이동이 됨.. 이동 안하고 처리???
    # return render(request, 'message_view.html', {})

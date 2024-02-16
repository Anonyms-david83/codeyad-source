from django.shortcuts import render , HttpResponse
from django.http import Http404

users = [
    {
        'username' : 'amir',
        'name' : 'amirhossein',
        'lastname' : 'amir',
        'phone' : '093785211',
        'city' : 'ahvaz'

    },
    {
        'username': 'ali',
        'name': 'hossein',
        'lastname': 'mamadi',
        'phone': '0937857888',
        'city': 'qom'

    },
    {
        'username': 'ali',
        'name': 'enayat',
        'lastname': 'koskhol',
        'phone': '0937888211',
        'city': 'tehron'

    },
]

def userlist(request):

    return render(request , 'account_app/user_list.html' , context={'users_list' : users}) #visit user_list.html for jinja template lanugage

def profile(request , temped_username):
    for user in  users:
        if user['username'] == temped_username:
            return render(request , 'account_app/profile.html' , context= {'user' : user})

    #return render(request , 'account_app/profile.html', context = {"username" : username}) #render accepts request and the template's directory  | # render( .. , context = value) -> we use key in {{}} in the frontend
                                                                         #   ^->  !!!!! in flask we say username = "ali" , we don't use context = dic in flask !!!!!

    return Http404('user not found') #Http404 return an 404 error with a custom message



def info (request):
    return render(request , 'account_app/info.html' )

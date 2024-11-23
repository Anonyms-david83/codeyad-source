from django.shortcuts import render , HttpResponse



users = ['amir' , 'milad' , 'hossein' , 'ali' , 'farid' , 'reza']
blocked_users = ['milad' , 'ali']

def profile(request , username):
    if username in users:
        if username in blocked_users:
            return HttpResponse(f'<h1 style="color:red"> {username} is blocked</h1>')
        return HttpResponse(f'hi {username}')

    else:
        return HttpResponse(f'<h1 style="color:red"> {username} is a wrong username</h1>')



def info (request , username):
    return HttpResponse(f'hi from info')

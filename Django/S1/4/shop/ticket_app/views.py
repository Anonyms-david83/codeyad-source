from django.shortcuts import render
from .models import Ticket

def add_ticket(request):
    attemped_title = request.GET.get('title')
    attemped_body = request.GET.get('body')

    if attemped_body and attemped_title :
        Ticket.objects.create(title=attemped_title , body=attemped_body)
    return render(request , "ticket_app/add_ticket.html")

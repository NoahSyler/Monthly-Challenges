from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    'january': 'Get to the gym',
    'february': 'Sharpen JavaScript skills',
    'march': 'Learn React',
    'april': 'Practice with Django',
    'may': 'Practice with Django and React',
    'june': 'Study a functional programming language',
    'july': 'Apply rhe new concepts into current code',
    'august': 'Build an API',
    'september': 'Build a website',
    'october': 'Build a mobile App',
    'november': 'Build test cases',
    'december': 'Get some sleep'
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html",{
        "months": months
    })
    """ for month in months:
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data) """

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('My man, what are you doing?')
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    #try:
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {
        "text": challenge_text,
        "month_name": month
        })
        
    #except:
    #    return HttpResponseNotFound('<h1>this month is not supported</h1>')
    

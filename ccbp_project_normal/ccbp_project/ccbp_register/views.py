from django.shortcuts import render

def registration_form(request):
    return render(request, 'ccbp_register/register_form.html')

def player_list(request):
    return render(request, 'ccbp_register/players_list.html')
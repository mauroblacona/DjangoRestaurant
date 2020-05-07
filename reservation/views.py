from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Reservation
from .forms import ReserveTableForm

def reserve_table(request):
    reserve_form = ReserveTableForm()
    success = False
    
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        
        if reserve_form.is_valid():
            reserve_form.save()    
            reserve_form = ReserveTableForm()
            success = True
    
    context = {'form': reserve_form}
    
    return render(request, 'Reservation/reservation.html', context)

from django.shortcuts import render
from .models import Pharmacy

def pharmacy_list(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'pharmacy/pharmacy_list.html', {'pharmacies': pharmacies})

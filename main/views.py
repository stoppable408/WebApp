from django.shortcuts import render
from django.http import HttpResponse
import sorter
import csv
# Create your views here.
def home(request):
    final_list = sorter.createFinalList(sorter.create_violation_list())
    p = open(r'C:\Users\Solomon\Documents\GitHub\WebApp\main\templates\main\final.csv', 'wb')
    writer = csv.writer(p)
    writer.writerows(final_list)
    return render(request, "main/home.html")
def final(request):
    return render(request, "main/final.csv")

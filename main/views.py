from django.shortcuts import render
from django.http import HttpResponse
import sorter
# Create your views here.
def home(request):
    violation_list = sorter.create_violation_list()
    final_list = sorter.createFinalList(violation_list)
    json = sorter.final_list_to_json(final_list)
    return render(request, "main/home.html", {'message': json})

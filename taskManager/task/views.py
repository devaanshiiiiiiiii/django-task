from django.shortcuts import render,HttpResponse
from .forms import userForm
import pandas as pd
from django.http import HttpResponse
from .models import Task,user
def test(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('DONE!')
    else:
        form = userForm()
        return render(request, 'index.html', {'form': form})

    return render(request,"index.html")


def Task_dataTOexcel(request):
    queryset = Task.objects.all()
    df = pd.DataFrame(list(queryset.values()))
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Task.xlsx"'
    df.to_excel(response, index=False)

    return response

def user_dataTOexcel(request):
    queryset = user.objects.all()
    df = pd.DataFrame(list(queryset.values()))
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="user.xlsx"'
    df.to_excel(response, index=False)

    return response
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .form import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.
class Tasllistview(ListView):
    model = Task
    template_name = "add.html"
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Task
    template_name = "detail.html"
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = Task
    template_name = "update1.html"
    context_object_name = 'task'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy("cbvadd")


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get("Task")
        priority = request.POST.get("Priority")
        date = request.POST.get("Date")
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"add.html",{'task1':task1})
# def detail(request):
#     return render(request,"detail.html",)
def delete(request,id):
    if request.method=='POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,'task':task})
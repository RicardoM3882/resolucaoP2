from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todo_list'

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline', 'finished_at']
    template_name = 'todo_form.html'
    success_url = reverse_lazy('todo_list')
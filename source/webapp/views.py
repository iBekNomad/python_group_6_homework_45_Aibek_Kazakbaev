from django.shortcuts import render
from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data,
    })


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        task = Article.objects.create(description=description, status=status)
        context = {'task': task}
        return render(request, 'task_view.html', context)




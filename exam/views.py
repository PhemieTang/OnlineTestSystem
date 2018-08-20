from django.shortcuts import render


def teacher(request):
    return render(request, 'exam/make-questions.html')


def edit(request):
    return render(request, 'exam/edit.html')


def mark(request):
    return render(request, 'exam/give-a-mark.html')


def homepage(request):
    return render(request, 'exam/home.html')



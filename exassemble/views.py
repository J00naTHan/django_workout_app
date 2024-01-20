from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from .models import Exercise, ExerciseSheet
from .forms import ExerciseForm, SheetForm
from django.contrib.auth.decorators import login_required
from django import forms


# view que retorna uma lista das planilhas criadas e renderiza um template passando essa lista como var
def index(request):
    user = request.user
    if user.is_authenticated:
        sheets = ExerciseSheet.objects.filter(creator=user)
        if user.get_short_name():
            username = user.get_short_name()
            return render(request, 'index.html', {'sheets': sheets, 'username': username})
        else:
            username = user.get_username()
            return render(request, 'index.html', {'sheets': sheets, 'username': username})
    else:
        username = False
        sheets = False
        return render(request, 'index.html', {'sheets': sheets, 'username': username})


# view que retorna uma lista dos exercícios criados e renderiza uma template passando essa lista como var
def listExercises(request):
    try:
        exercises = Exercise.objects.all()
    except Exercise.DoesNotExist:
        raise Http404(render(request, '404.html'))
    return render(request, 'exercise_list.html', {'exercises': exercises})


# view que retorna uma planilha por um id passado na URL, e então renderiza um template com a planilha como var
@login_required
def viewSheet(request, pk):
    try:
        sheet = ExerciseSheet.objects.get(id=pk)
    except ExerciseSheet.DoesNotExist:
        raise Http404(render(request, '404.html'))
    return render(request, 'sheet_detail.html', context={'sheet': sheet})


# view que retorna um exercício por um id passado na URL, e então renderiza um template com o exercício como var
@login_required
def viewExercise(request, pk):
    try:
        exercise = Exercise.objects.get(id=pk)
    except Exercise.DoesNotExist:
        raise Http404(render(request, '404.html'))
    return render(request, 'exercise_detail.html', {'exercise': exercise})


@login_required
def addExercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            creator = form.cleaned_data["creator"]
            creator = User.objects.get(username=creator)
            description = form.cleaned_data["description"]
            exercise = Exercise(name=name, creator=creator, description=description)
            exercise.save()
            return HttpResponseRedirect("/app/exercises/")
    else:
        pre_creator = request.user.username
        creator = User.objects.get(username=pre_creator)
        form = ExerciseForm(initial={'creator': creator})
        form.fields['creator'].widget = forms.HiddenInput(attrs={'readonly': 'readonly'})
    return render(request, 'addexercise.html', {"form": form})


@login_required
def addSheet(request):
    if request.method == 'POST':
        form = SheetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pre_creator = form.cleaned_data['creator']
            creator = User.objects.get(username=pre_creator)
            exercises = form.cleaned_data['exercises']
            sheet = ExerciseSheet(name=name, creator=creator)
            sheet.save()
            sheet.exercises.set(exercises)
            sheet.save()
            return HttpResponseRedirect('/app/')
    else:
        pre_creator = request.user.username
        creator = User.objects.get(username=pre_creator)
        form = SheetForm(initial={'creator': creator})
        form.fields['creator'].widget = forms.HiddenInput(attrs={'readonly': 'readonly'})
    return render(request, 'addsheet.html', {'form': form})


@login_required
def updateExercise(request, pk):
    try:
        exercise = Exercise.objects.get(id=pk)
    except Exercise.DoesNotExist:
        raise Http404(render(request, '404.html'))
    if request.method == 'GET':
        form = ExerciseForm(instance=exercise)
        model = 'exercise'
        form.fields['creator'].widget = forms.HiddenInput(attrs={'readonly': 'readonly'})
    else:
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            url = f'/app/exercises/{exercise.id}/'
            return HttpResponseRedirect(url)
    return render(request, 'update.html', context={'form': form, 'id': exercise.pk, 'model':model})

@login_required
def deleteExercise(request, pk):
    try:
        exercise = Exercise.objects.get(id=pk)
    except Exercise.DoesNotExist:
        raise Http404(render(request, '404.html'))
    exercise.delete()
    url = reverse('exercises')
    return redirect(url)


# view que deleta uma planilha do db pelo id, e redireciona o usuário para a URL base
@login_required
def deleteSheet(request, pk):
    try:
        sheet = ExerciseSheet.objects.get(id=pk)
    except ExerciseSheet.DoesNotExist:
        raise Http404(render(request, '404.html'))
    sheet.delete()
    url = reverse('index')
    return redirect(url)


# view que busca uma planilha por id, e renderiza um formulário que conterá os novos dados para essa planilha
@login_required
def updateSheet(request, pk):
    try:
        sheet = ExerciseSheet.objects.get(id=pk)
    except ExerciseSheet.DoesNotExist:
        raise Http404(render(request, '404.html'))
    if request.method == 'GET':
        form = SheetForm(instance=sheet)
        model = 'sheet'
        form.fields['creator'].widget = forms.HiddenInput(attrs={'readonly': 'readonly'})
    else:
        form = SheetForm(request.POST, instance=sheet)
        if form.is_valid():
            form.save()
            url = f'/app/{sheet.id}/'
            return HttpResponseRedirect(url)
    return render(request, 'update.html', {'form': form, 'id': sheet.pk, 'model': model})

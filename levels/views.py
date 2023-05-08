from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TreasureHunt
import random
# Create your views here.

def home(request):
    return render(request,'levels/home.html')

def about(request):
    return render(request,'levels/about.html')


def treasurehunt_list(request):
    treasurehunts = TreasureHunt.objects.all()
    print(TreasureHunt.objects.count())
    numbers=[8,16,24]
    context = {
        'treasurehunts':treasurehunts,
        'numbers':numbers,
    }
    return render(request, 'levels/treasurehunt_list.html', context)

@login_required
def level1(request):
    if request.method=='POST':
        answer=request.POST.get('level1')
        print(answer)
        if answer.lower() == '13000':
            messages.success(request,"Hurray! you got it, It's correct. You had completed task in The Great Wall of China and can now go to another place Petra - Jordan")
            treasure_hunt = TreasureHunt.objects.create(user=request.user, level=1, answer=answer, score = 5,totscore = 5)
            treasure_hunt.save()
            return redirect('level2')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('level1')
    return render(request,'levels/level1.html')

@login_required
def level2(request):
    if request.method=='POST':
        answer=request.POST.get('level2')
        print(answer)
        lscore = 5
        if answer.lower() == 'rose city' or answer.lower() == 'rosecity':
            messages.success(request,"Hurray! you got it, It's correct. You had completed task in Petra - Jordan and can now go to another place Christ the Redeemer - Brazil")
            treasure_hunt = TreasureHunt.objects.create(user=request.user, level=2, answer=answer,score = lscore, totscore = 5)
            treasure_hunt.save()
            return redirect('level3')
        else:
            if 'counter' not in request.session:
                request.session['counter'] = 1
                lscore = 5
            else:
                request.session['counter'] += 1
                lscore = 5 - request.session['counter']
            if request.session['counter'] >= 5:
                messages.error(request, "You have exceeded the maximum number of attempts. Please login again to retry.")
                return redirect('home')
            messages.warning(request, "Incorrect Answer")
            return redirect('level2')
    return render(request,'levels/level2.html')

@login_required
def level3(request):
    if request.method=='POST':
        answer=request.POST.get('level3')
        print(answer)
        if answer=='600':
            messages.success(request,"Hurray! you got it, It's correct. You had completed task in Christ the Redeemer - Brazil and now its time to play a game of identifying colors")
            # answer = form.cleaned_data['answer']
            treasure_hunt = TreasureHunt.objects.create(user=request.user, level=3, answer=answer, score = 5, totscore = 5)
            treasure_hunt.save()
            return redirect('level4')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('level3')
    return render(request,'levels/level3.html')


@login_required
def level4(request):
    colors =['Black', 'Red', 'Blue', 'Green', 'Pink', 'Purple', 'Brown', 'Yellow', 'Orange', 'White']
    score = request.session.get('score', 0)
    color_name = random.choice(colors)
    color_code = request.session.get('color_code', random.choice(colors))
    num_chances = request.session.get('num_chances', 10)
    if request.method == 'POST':
        guess = request.POST.get('level4', '').lower()
        color = color_code.lower()
        if guess == color:
            score += 1
        request.session['score'] = score
        num_chances -= 1
        print(num_chances)
        request.session['num_chances'] = num_chances
        if num_chances == 0:
            if score >= 6:
                lscore = score
                messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
                treasure_hunt = TreasureHunt.objects.create(user=request.user, level=4, answer=score, score = lscore, totscore = 10)
                treasure_hunt.save()
                return redirect('level5')
            else:
                return redirect('game_over')

        color_code = random.choice(colors)
        request.session['color_code'] = color_code

    context = {
        'color_name': color_name,
        'color_code': color_code,
        'score': score,
        'num_chances': num_chances,
    }
    return render(request, 'levels/level4.html', context)


def game_over(request):
    request.session.flush()  # clear all session data
    return render(request, 'levels/game_over.html')


@login_required
def level5(request):
    if request.method=='POST':
        answer=request.POST.get('level5')
        if answer.lower() == "quechua":
            messages.success(request,"Hurray! you got it, It's correct. You had completed task and now its time to complete in Chichen Itza - Mexico")
            # answer = form.cleaned_data['answer']
            treasure_hunt = TreasureHunt.objects.create(user=request.user, level=5, answer=answer, score = 5, totscore = 5)
            treasure_hunt.save()
            return redirect('level6')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('level5')
    return render(request,'levels/level5.html')


@login_required
def level5a(request):
    return render(request,'levels/level5a.html')

@login_required
def level6(request):
    if request.method=='POST':
        answer=request.POST.get('level6')
        print(answer)
        if answer=='365':
            messages.success(request,"Hurray! you got it, It's correct. You had completed task in Chichen Itza - Mexico and now its time to complete in Colosseum - Italy")
            # answer = form.cleaned_data['answer']
            treasure_hunt = TreasureHunt.objects.create(user=request.user, level=6, answer=answer, score = 5, totscore = 5)
            treasure_hunt.save()
            return redirect('level7')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('level6')
    return render(request,'levels/level6.html')

@login_required
def level7(request):
    if request.method=='POST':
        answer=request.POST.get('level7')
        print(answer)
        score = 10
        if answer.lower() == 'travertine limestone' or answer.lower() == 'travertinelimestone':
            messages.success(request,"Hurray! you got it, It's correct. You had completed task in Colosseum - Italy and now its time to complete in Taj Mahal - India")
            treasure_hunt = TreasureHunt.objects.create(user=request.user, level=7, answer=answer, score = score, totscore = 10)
            treasure_hunt.save()
            return redirect('level8')
        else:
            if 'counter' not in request.session:
                request.session['counter'] = 1
            else:
                request.session['counter'] += 1
            if request.session['counter'] >= 5:
                messages.error(request, "You have exceeded the maximum number of attempts. Please login again to retry.")
                return redirect('home')
            messages.warning(request, "Incorrect Answer")
            score = 10 - request.session['counter']
            return redirect('level7')
    return render(request,'levels/level7.html')

@login_required
def level8(request):
    if request.method=='POST':
        answer=request.POST.get('level8')
        if answer.lower()=="yamuna":
            messages.success(request,"Hurray! you got it, It's correct. You had completed all tasks friend")
            # answer = form.cleaned_data['answer']
            treasure_hunt = TreasureHunt.objects.create(user=request.user, level=8, answer=answer, score = 5, totscore = 5)
            treasure_hunt.save()
            return redirect('final')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('level8')
    return render(request,'levels/level8.html')


def final(request):
    return render(request,'levels/final.html')

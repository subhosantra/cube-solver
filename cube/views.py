from django.shortcuts import render
from django.http import HttpResponse
from cube.rubik import test, startpoint, search, rotate, tools, color, corner, coordcube, edge, facecube, facelet, cubiecube, cam
# Create your views here.

def home(request):
    return render(request, "cube/index.html")

def solve(request):
    if request.method == "POST" :
        cubestring = request.POST['cubestring']
        # print(cubestring)
        # test.sol(cubestring)
        errors = {
            'Error 1': 'There is not exactly one facelet of each colour',
            'Error 2': 'Not all 12 edges exist exactly once',
            'Error 3': 'Flip error: One edge has to be flipped',
            'Error 4': 'Not all corners exist exactly once',
            'Error 5': 'Twist error: One corner has to be twisted',
            'Error 6': 'Parity error: Two corners or two edges have to be exchanged',
            'Error 7': 'No solution exists for the given maxDepth',
            'Error 8': 'Timeout, no solution within given time'
        }
        ans = startpoint.solve((str(cubestring)))
        if ans in errors:
            return HttpResponse(errors[ans])
        else:
            # print(ans)
            return HttpResponse(ans)
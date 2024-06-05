from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# neg url deer olon service bna tuedniig dict keyeer ylgaj ugnu
# method, if json, key, value bugdiin shalgah

def today(request):
    res = {'today': datetime.today().strftime('%Y-%m-%d')}
    return res


def current_time(request):
    res = {'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    # current_time = {'current_time': datetime.now()}
    # res = json.dumps(current_time, indent=4,
    #                  sort_keys=True, default=str)
    # return JsonResponse(json.loads(res))
    return res

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            req_body = json.loads(request.body)
            action = req_body['action']
            if action == 'today':
                t = today(request)
                return JsonResponse(t)
            elif action == 'current':
                c = current_time(request)
                return JsonResponse(c)

            else:
                return JsonResponse({'error': 'not found value'})
        except:
            return JsonResponse({'error': 'invalid action'})
    else:
        return JsonResponse({'error': 'wrong method'})

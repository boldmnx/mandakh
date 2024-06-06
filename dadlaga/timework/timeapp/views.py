from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from timework.settings import *


# neg url deer olon service bna tuedniig dict keyeer ylgaj ugnu
# method, if json, key, value bugdiin shalgah

def today(request):
    jsons = json.loads(request.body)
    ttime = datetime.today().strftime('%Y-%m-%d')
    data = {'today': ttime}
    action = jsons['action']
    result = sendResponse(200, data, action)
    return result


def current_time(request):
    jsons = json.loads(request.body)
    ttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = [{'current_time': ttime}]
    action = jsons['action']
    result = sendResponse(200, data, action)
    return result


def get_t_asuult(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    onn = jsons['onn']
    hicheelkod = jsons['hicheelkod']
    huvilbar = jsons['huvilbar']
    asuulttoo = jsons['asuulttoo']

    con = connectionDB()
    cur = con.cursor()
    cur.execute(f'''
                SELECT * FROM mttest.t_asuult
                WHERE
                    onn= {onn} and
                    hicheelkod = {hicheelkod} and
                    huvilbar = '{huvilbar}'
                    ORDER BY random() LIMIT {asuulttoo}
                ''')
    colums=cur.description
    respRow=[{
        colums[index][0]:column for index,column in enumerate(value )} for value in cur.fetchall()]
    
    disconnectDB(con)
    result = sendResponse(200, respRow, action)
    return result


@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            jsons = json.loads(request.body)
        except Exception as e:
            a = 'wrong json'
            result = sendResponse(404, [e], a)
            return JsonResponse(json.loads(result))
        if 'action' in jsons:
            action = jsons['action']
            if action == 'today':
                t = today(request)
                return JsonResponse(json.loads(t))
            elif action == 'current':
                c = current_time(request)
                return JsonResponse(json.loads(c))
            elif action == 't_asuult':
                res = get_t_asuult(request)
                print(res)
                return JsonResponse(json.loads(res))
            else:
                action = 'action олдсонгүй'
                result = sendResponse(404, [], action)
                return JsonResponse(json.loads(result))
        else:
            action = 'action байхгүй'
            result = sendResponse(404, [], action)
            return JsonResponse(json.loads(result))

    else:
        method = 'wrong method'
        result = sendResponse(404, [], method)
        return JsonResponse(json.loads(result))

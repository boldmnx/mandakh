from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from whois.settings import sendResponse, connectDB, disconnectDB


# def getPerson(request):
#     jsons = json.loads(request.body)
#     action = jsons['action']
#     pid = jsons['pid']
#     con = connectDB()
#     cur = con.cursor()
#     query = f'''SELECT 
#     pd.firstname, 
#     pd.lastname, 
#     pd.headline, 
#     pd.address, 
#     pd.phone, 
#     pd.email, 
#     pd.linkedin, 
#     pd.github, 
#     pd.facebook, 
#     pd.city, 
#     pd.summary,
#     json_agg(json_build_object(
#         'institution', e.institution,
#         'location', e.location,
#         'start_year', e.start_year,
#         'graduation_year', e.graduation_year,
#         'description', e.description
#     )) AS education,
#     json_agg(json_build_object(
#         'job_title', ex.job_title,
#         'company', ex.company,
#         'location', ex.location,
#         'start_date', ex.start_date,
#         'end_date', ex.end_date,
#         'responsibilities', ex.responsibilities
#     )) AS experience,
#     json_agg(json_build_object(
#         'skill', s.skill
#     )) AS skills,
#     json_agg(json_build_object(
#         'name', c.name,
#         'institution', c.institution,
#         'year', c.year
#     )) AS certifications,
#     json_agg(json_build_object(
#         'name', p.name,
#         'description', p.description,
#         'url', p.url
#     )) AS projects,
#     json_agg(json_build_object(
#         'language', l.language
# 	)) AS languages,
#     json_agg(h.hobbies) AS hobbies
# FROM 
#     whois.t_person_details pd
# LEFT JOIN whois.t_education e ON pd.pid = e.pid 
# LEFT JOIN whois.t_experience ex ON pd.pid = ex.pid 
# LEFT JOIN whois.t_skills s ON pd.pid = s.pid 
# LEFT JOIN whois.t_certifications c ON pd.pid = c.pid 
# LEFT JOIN whois.t_projects p ON pd.pid = p.pid 
# LEFT JOIN whois.t_languages l ON pd.pid = l.pid 
# LEFT JOIN whois.t_hobbies h ON pd.pid = h.pid 
# where pd.pid={pid}
# GROUP BY pd.pid;'''
#     cur.execute(query)
#     columns = cur.description
#     respRow = [{columns[index][0]: column
#                 for index, column in enumerate(value)} for value in cur.fetchall()]
#     cur.close()
#     disconnectDB(con)
#     return sendResponse(200, respRow, action)


def cv_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            fname = data['firstname']
            con = connectDB()
            cur = con.cursor()
            cur.execute(f'''insert into whois.t_person_details(firstname)
                            VALUES('{fname}')''')
            print('------------------------------------'+fname)
            cur.close()
            con.commit()
            disconnectDB()
            respRow = {'kakak': 'sa'}
            return sendResponse(200, respRow)
        except Exception as e:
            return e


@csrf_exempt
def home(request):
    if request.method == "POST":
        try:
            jsons = json.loads(request.body)
        except json.JSONDecodeError:
            action = "wrong json"
            data = []
            result = sendResponse(404, data, action)
            return JsonResponse(json.loads(result))
        if 'action' in jsons:
            action = jsons['action']
            if action == "cv_register":
                result = cv_register(request)
                return JsonResponse(json.loads(result))
            else:
                action = "action not found"
                data = []
                result = sendResponse(404, data, action)
                return JsonResponse(json.loads(result))

        else:
            action = "no action"
            data = []
            result = sendResponse(404, data, action)
            return JsonResponse(json.loads(result))
    else:
        action = "method buruu"
        data = []
        result = sendResponse(405, data, action)
        return JsonResponse(json.loads(result))

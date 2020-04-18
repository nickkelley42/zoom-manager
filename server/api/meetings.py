import zoom
import request
import forms
from os import environ

def meetings_actions() :
    method = environ['REQUEST_METHOD']
    if method == 'GET':
        get_all_meetings()
    elif method == 'POST':
        create_meeting()
    else:
        res = request.Response()
        res.status = 400
        res.data = 'Bad request'
        res.send()

def get_single_meeting():
    response = request.Response()
    request.status = 500
    request.data = 'not implemented yet'
    request.send()

def create_meeting():
    response = request.Response()
    req_data = forms.get_form_data()

    if 'data' not in req_data or 'attributes' not in req_data['data']:
        _create_failure(response)
        return
    data = req_data['data']['attributes']

    if 'topic' not in data or 'start-time' not in data:
        _create_failure(response)
        return
    
    topic = data['topic']
    start = data['start-time']
    new_meeting = zoom.create_meeting(topic=topic, start_string=start)
    response.data = {
        'data': _meeting_to_ember(new_meeting)
    }
    response.send()

def _create_failure(response, status=400, message="Bad request"):
    response.status = status
    response.message = message
    response.send()

def get_all_meetings():
    meetings = zoom.get_meetings()
    resp_meetings = []

    for meeting in meetings:
        formatted = _meeting_to_ember(meeting)
        resp_meetings.append(formatted)

    response = request.Response()
    response.data = { 'data': resp_meetings }
    response.send()

def _meeting_to_ember(meeting):
    formatted = {
        'type': 'meetings',
        'id': meeting['id'],
        'attributes': {
            'topic': meeting['topic'],
            'start-time': meeting['start_time'],
            'join-url': meeting['join_url'],
            'duration': meeting['duration'],
        }
    }
    return formatted

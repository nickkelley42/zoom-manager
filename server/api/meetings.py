import zoom
import request

def get_all_meetings():
    meetings = zoom.get_meetings()
    resp_meetings = []

    for meeting in meetings:
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
        resp_meetings.append(formatted)

    response = request.Response()
    response.data = { 'data': resp_meetings }
    response.send()

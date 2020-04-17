import zoom
import request

def get_all_meetings():
    meetings = zoom.get_meetings()
    response = request.Response()
    response.data = { 'meeting': meetings }
    response.send()

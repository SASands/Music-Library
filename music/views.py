from rest_framework.decorators import api_view
from rest_framework.response import Response

# Define all of the functions for user interaction here
@api_view(['GET'])
def songs_list(request):
    

    return Response('OK')

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def geRoutes(request):
    routes = [
        "GET /api/",
        "GET /api/rooms",
        "GET /api/rooms/:id",
    ]
    return Response(routes)   
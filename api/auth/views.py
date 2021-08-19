from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer

class ProfileView(APIView):
    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
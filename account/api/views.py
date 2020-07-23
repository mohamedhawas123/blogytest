from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from account.api.serializers import RegisterSerializer


@api_view(['POST'])
def register_view(request):

    if request.method == "Post":
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "success"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)

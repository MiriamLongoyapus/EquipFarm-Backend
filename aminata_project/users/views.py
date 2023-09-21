# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import CustomUser

# class UserTypeInfoView(APIView):
#     def get(self, request):
#         user = request.user  # Get the currently logged-in user

#         if user.is_authenticated:
#             if user.is_farmer():
#                 # The user is a farmer
#                 return Response({'message': 'You are a farmer.'}, status=status.HTTP_200_OK)
#             elif user.is_supplier():
#                 # The user is a supplier
#                 return Response({'message': 'You are a supplier.'}, status=status.HTTP_200_OK)
#             else:
#                 # The user doesn't have a specific role
#                 return Response({'message': 'You are a registered user, but not a farmer or supplier.'}, status=status.HTTP_200_OK)
#         else:
#             # The user is not authenticated
#             return Response({'message': 'You are not logged in.'}, status=status.HTTP_401_UNAUTHORIZED)

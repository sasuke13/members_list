from typing import Optional

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.base_api import ApiBaseView
from core.containers import UserContainer
from users.DTOs import UserDTO
from users.exceptions import UserDoesNotExist
from users.serializers import UserSerializer


class UserAPIView(APIView, ApiBaseView):
    __user_interactor = UserContainer.interactor()

    def get(self, request, id: Optional[int] = None):
        if id:
            key_for_response = 'user_by_id'

            try:
                user = self.__user_interactor.get_user_dto_by_id(id)
            except UserDoesNotExist as exception:
                return self._create_response_not_found(exception)

            serialized_user = UserSerializer(user)

        else:
            key_for_response = 'users'

            users = self.__user_interactor.get_all_users_dto()

            serialized_user = UserSerializer(users, many=True)

        return Response({key_for_response: serialized_user.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_user_data = UserSerializer(data=request.data)

        is_serialized_user_data_valid = serialized_user_data.is_valid()

        if not is_serialized_user_data_valid:
            return self._create_response_for_invalid_serializers(serialized_user_data)

        user_data_dto = UserDTO(**serialized_user_data.validated_data)

        created_user = self.__user_interactor.create_user(user_data_dto)

        serialized_user = UserSerializer(created_user)

        return Response(
            {
                'message': 'User was successfully added to member list',
                'user': serialized_user.data
            },
            status=status.HTTP_201_CREATED
        )

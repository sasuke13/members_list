from typing import Iterable

from annoying.functions import get_object_or_None


from users.DTOs import UserDTO
from users.exceptions import UserDoesNotExist
from users.interfaces import UserRepositoryAndServiceInterface
from users.models import Users


class UserRepository(UserRepositoryAndServiceInterface):
    def create_user(self, user_data_dto: UserDTO) -> Users:
        user = Users.objects.create(**user_data_dto.__dict__)

        return user

    def get_user_by_id(self, id: int) -> Users:
        user = get_object_or_None(Users, id=id)

        if not user:
            raise UserDoesNotExist(f'User with id {id} does not exist!')

        return user

    def get_all_users(self) -> Iterable[Users]:
        users = Users.objects.all()

        return users

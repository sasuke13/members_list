from typing import Iterable


from users.DTOs import UserDTO
from users.interfaces import UserRepositoryAndServiceInterface
from users.models import Users


class UserService(UserRepositoryAndServiceInterface):
    def __init__(self, repository: UserRepositoryAndServiceInterface):
        self.repository = repository

    def create_user(self, user_data_dto: UserDTO) -> Users:
        return self.repository.create_user(user_data_dto)

    def get_user_by_id(self, id: int) -> Users:
        return self.repository.get_user_by_id(id)

    def get_all_users(self) -> Iterable[Users]:
        return self.repository.get_all_users()

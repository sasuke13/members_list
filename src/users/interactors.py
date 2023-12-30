from itertools import repeat
from typing import Iterable

from users.DTOs import UserDTO
from users.interfaces import UserInteractorInterface, UserRepositoryAndServiceInterface
from auto_dataclass.dj_model_to_dataclass import ToDTOConverter


class UserInteractor(UserInteractorInterface):
    def __init__(self, to_dto_converter: ToDTOConverter, user_service: UserRepositoryAndServiceInterface):
        self.to_dto_converter = to_dto_converter
        self.user_service = user_service

    def create_user(self, user_data_dto: UserDTO) -> UserDTO:
        created_user = self.user_service.create_user(user_data_dto)

        return self.to_dto_converter.to_dto(created_user, UserDTO)

    def get_user_dto_by_id(self, id: int) -> UserDTO:
        user = self.user_service.get_user_by_id(id)

        return self.to_dto_converter.to_dto(user, UserDTO)

    def get_all_users_dto(self) -> Iterable[UserDTO]:
        users = self.user_service.get_all_users()

        return map(self.to_dto_converter.to_dto, users, repeat(UserDTO))

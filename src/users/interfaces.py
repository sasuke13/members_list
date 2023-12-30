from abc import ABC, abstractmethod
from typing import Iterable



from users.DTOs import UserDTO
from users.models import Users


class UserRepositoryAndServiceInterface(ABC):
    @abstractmethod
    def create_user(self, user_data_dto: UserDTO) -> Users:
        pass

    @abstractmethod
    def get_user_by_id(self, id: int) -> Users:
        pass

    @abstractmethod
    def get_all_users(self) -> Iterable[Users]:
        pass


class UserInteractorInterface(ABC):
    @abstractmethod
    def create_user(self, user_data_dto: UserDTO) -> UserDTO:
        pass

    @abstractmethod
    def get_user_dto_by_id(self, id: int) -> UserDTO:
        pass

    @abstractmethod
    def get_all_users_dto(self) -> Iterable[UserDTO]:
        pass

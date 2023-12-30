from auto_dataclass.dj_model_to_dataclass import FromOrmToDataclass
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory

from users.interactors import UserInteractor
from users.repositories import UserRepository
from users.services import UserService


class ConvertorsContainer(DeclarativeContainer):
    from_queryset_to_dto = Factory(FromOrmToDataclass)


class RepositoryContainer(DeclarativeContainer):
    user_repository = Factory(UserRepository)


class ServiceContainer(DeclarativeContainer):
    user_service = Factory(
        UserService,
        repository=RepositoryContainer.user_repository
    )


class InteractorContainer(DeclarativeContainer):
    user_interactor = Factory(
        UserInteractor,
        to_dto_converter=ConvertorsContainer.from_queryset_to_dto,
        user_service=ServiceContainer.user_service
    )


class UserContainer(DeclarativeContainer):
    repository = RepositoryContainer.user_repository
    service = ServiceContainer.user_service
    interactor = InteractorContainer.user_interactor

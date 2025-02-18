# import services here
from services.user_service import UserService


class Service:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Service, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        # create instance of services
        self.user_service=UserService()

# create service instance
services = Service()
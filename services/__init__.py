# import services here
from services.user_service import UserService
from services.service_type_service import ServiceTypeService
from services.service_service import ServiceService


class Service:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Service, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        # create instance of services
        self.user_service=UserService()

    def __init__(self) -> None:
        # create instance of services
        self.service_type_service=ServiceTypeService()

    def __init__(self) -> None:
        # create instance of services
        self.service_service=ServiceService()

# create service instance
services = Service()





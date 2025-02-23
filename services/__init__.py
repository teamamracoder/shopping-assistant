# import services here
from services.user_service import UserService
from services.service_type_service import ServiceTypeService
from services.service_service import ServiceService
from services.service_booking_service import ServiceBookingService


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

    def __init__(self) -> None:
        # create instance of services
        self.service_booking_service=ServiceBookingService()

# create service instance
services = Service()





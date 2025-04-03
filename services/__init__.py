# import services here
from services.user_service import UserService
from services.service_type_service import ServiceTypeModelService
from services.service_service import ServiceService
from services.service_booking_service import ServiceBookingModelService
from services.manage_store_service import *

class Service:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Service, cls).__new__(cls)
        return cls._instance

    # def __init__(self) -> None:
    #     # create instance of services
    #     self.user_service=UserService()

    # def __init__(self) -> None:
    #     # create instance of services
    #     self.service_type_service=ServiceTypeModelService()

    # def __init__(self) -> None:
    #     # create instance of services
    #     self.service_service=ServiceService()

    # def __init__(self) -> None:
    #     # create instance of services
    #     self.service_booking_service=ServiceBookingModelService()


    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):  # ✅ Prevent re-initialization
            self.user_service = UserService()  # ✅ Initialize `user_service`
            self.service_type_service = ServiceTypeModelService()
            self.service_service = ServiceService()
            self.service_booking_service = ServiceBookingModelService()
            self.initialized = True  # ✅ Mark as initialized
# create service instance
services = Service()





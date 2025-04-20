# import services here
from services.user_service import UserService
from services.service_type_service import ServiceTypeModelService,ServiceTypeModelAPI
from services.service_service import ServiceService,ServiceModelAPI
from services.service_booking_service import ServiceBookingModelService
from services.manage_store_service import *
# from services.manage_product_sub_category_service import ProductSubCategoryModelService


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
        self.service_type_service=ServiceTypeModelService()

    def __init__(self) -> None:
        # create instance of services
        self.service_service=ServiceService()

    def __init__(self) -> None:
        # create instance of services
        self.service_booking_service=ServiceBookingModelService()


    def __init__(self) -> None:
        # create instance of services
        self.service_booking_service=ServiceBookingModelService()

    # def __init__(self) -> None:
    #     # create instance of services
    #     self.manage_product_sub_category_service=ProductSubCategoryModelService()


    # API Section

    def __init__(self) -> None:
        self.service_api = ServiceModelAPI()
        self.service_type_api = ServiceTypeModelAPI()

    



# create service instance
services = Service()



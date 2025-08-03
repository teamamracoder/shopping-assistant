# import services here
from services.user_service import UserService
from services.service_type_service import ServiceTypeModelService,ServiceTypeModelAPI
from services.service_service import ServiceService,ServiceModelAPI
from services.service_booking_service import ServiceBookingModelService
from services.manage_store_service import *
from services.product_service import *
from services.product_category_service import *
from services.product_sub_category_service import *
# from services.manage_product_sub_category_service import ProductSubCategoryModelService
from services.store_service import storeModelService
from services.store_category_service import StoreCategoryService
from services.email_track_service import *

class Service:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Service, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
            # create instances of all services
            self.user_service = UserService()
            self.service_type_service = ServiceTypeModelService()
            self.service_service = ServiceService()
            self.service_booking_service = ServiceBookingModelService()
            self.product_service = ProductModelService()
            self.product_category_service = ProductCategoryModelService()
            self.product_sub_category_service = ProductSubCategoryModelService()
            # self.manage_product_sub_category_service = ProductSubCategoryModelService()  # optional
            self.service_api = ServiceModelAPI()
            self.service_type_api = ServiceTypeModelAPI()
            self.store_service = storeModelService()
            self.store_category_service = StoreCategoryService()
            self.email_track_service= EmailTrackService()

services = Service()



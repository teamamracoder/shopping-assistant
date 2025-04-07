# from .demo_view import DemoView
from .home_view import IndexView
from .manage_dashboard_view import ManageDashboardView
from .manage_user_view import ManageUserCreateView,ManageUserDeleteView,ManageUserUpdateView,ManageUserListView
from .manage_store_view import *

from .manage_product_sub_category_view import ManageProductSubCategoryListView,ManageProductSubCategoryCreateView,ManageProductSubCategoryEditView,ManageProductSubCategoryDeleteView,ManageToggleProductSubCategoryActiveView
from .manage_product_view import ManageProductListView, ManageProductCreateView,ManageProductEditView,ManageProductDeleteView,ManageToggleProductActiveView
from .manage_product_category_view import ManageProductCategoryListView, ManageProductCategoryCreateView,ManageProductCategoryEditView,ManageProductCategoryDeleteView,ManageToggleProductCategoryActiveView

from .manage_service_type_view import ManageServiceTypeView, ManageCreateServiceTypeView

from .manage_template_view import ManageTemplateListView,ManageTemplateCreateView,ManageToggletemplatesActiveView

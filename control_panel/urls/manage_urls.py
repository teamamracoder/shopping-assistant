from django.urls import path


# from control_panel.views import ManageServiceTypeListView,ServiceBookingCreateView, ManageServiceTypeCreateView, ManageServiceTypeUpdateView,ManageServiceTypeDeleteView,ServiceBookingUpdateView,ManageToggleServiceTypeActiveView
# from control_panel.views import IndexView,ManageStoreView,ServiceBookingDeleteView,ManageServiceModelDeleteView,ManageServiceModelUpdateView,ManageServiceModelListView,ManageServiceModelCreateView,ManageDashboardView,ManageServiceTypeView,ManageUserCreateView,ManageUserDeleteView,ManageUserUpdateView,IndexView,ManageDashboardView,ManageProductSubCategoryListView,ManageProductSubCategoryCreateView,ManageProductCategoryEditView,ManageProductSubCategoryDeleteView,ManageToggleProductSubCategoryActiveView,ManageProductListView,ManageProductCreateView,ManageProductDeleteView,ManageToggleProductActiveView,ManageProductCategoryListView,ManageProductCategoryCreateView,ManageProductCategoryDeleteView,ManageToggleProductCategoryActiveView,ManageUserListView,ManageTemplateListView,ManageTemplateCreateView,ManageTemplateEditView,ManageTemplateDeleteView,ManageToggletemplatesActiveView
from control_panel.views import *

# app_name = 'user_management'  # Set the app namespace here

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', ManageDashboardView.as_view(), name='manage_dashboard'),

# user url by tufan
    path('users/', ManageUserListView.as_view(), name='manage_user_list'),
    path('users/create/', ManageUserCreateView.as_view(), name='manage_user_create'),
    path('admin/users/update/<int:pk>/', ManageUserUpdateView.as_view(), name='manage_user_update'),
    path('users/delete/<int:user_id>/', ManageUserDeleteView.as_view(), name="manage_user_delete"),
    # path('users/toggle-active/<int:pk>/', ManageToggleUserActiveView.as_view(), name='manage_toggle_user_active'),
    path('manage/user/toggle/<int:pk>/', ManageToggleUserActiveView.as_view(), name='manage_toggle_user_active'),

# service_model urls by tufan
    path('services_model/', ManageServiceModelListView.as_view(), name='manage_service_list'),
    path('services_model/create/', ManageServiceModelCreateView.as_view(), name='manage_create_service_model'),
    path('services_model/update/<int:pk>/', ManageServiceModelUpdateView.as_view(), name='manage_update_service_model'),
    path('services_model/delete/<int:pk>/', ManageServiceModelDeleteView.as_view(), name='manage_delete_service_model'),
    path('services_model/toggle/<int:pk>/', ManageToggleServiceModelActiveView.as_view(), name='manage_toggle_service_active'),
    
# service type model urls by tufan
    path('services-type/', ManageServiceTypeListView.as_view(), name='manage_service_type_model_list'),
    path('services-type/create/', ManageServiceTypeCreateView.as_view(), name='manage_service_type_model_create'),
    path('services-type/update/<int:pk>/', ManageServiceTypeUpdateView.as_view(), name='manage_service_type_model_update'),
    path('services-type/delete/<int:pk>/', ManageServiceTypeDeleteView.as_view(), name='manage_service_type_model_delete'),
    path('services-type/toggle/<int:pk>/', ManageToggleServiceTypeActiveView.as_view(), name='manage_toggle_service_type_active'),

#service_booking_model url by tufan 
# # JUST ADD PREFIX Manage in clss name
    path('service-bookings/create/', ManageServiceBookingCreateView.as_view(), name='manage_service_booking_create'),
    path('service-bookings/update/<int:pk>/', ManageServiceBookingUpdateView.as_view(), name='manage_service_booking_update'),
    path('service-bookings/delete/<int:pk>/', ManageServiceBookingDeleteView.as_view(), name='manage_service_booking_delete'),
    path('service-bookings/toggle/<int:pk>/', ManageToggleServiceBookingActiveView.as_view(), name='manage_service_booking_active'),



# store urls by priya
    # path('stores/', ManageStoreView.as_view(), name='manage_Store_list'),
    # path('stores/create/', ManageCreateStore.as_view(), name='manage_create_store'),
    # path('stores/update/<int:pk>/', ManageUpdateStoreView.as_view(), name='manage_update_store'),
    # path('toggle-store-status/<int:store_id>/', ToggleStoreStatus.as_view(), name='toggle_store_status'),

#store category url
    path('stores/category/', ManageStoreCategoryView.as_view(), name='manage_Store_category_list'),
    path('store-category/create/', ManageCreateStoreCategoryView.as_view(), name='manage_create_store_category'),
    path("store-category/delete/<int:category_id>/", ManageDeleteStoreCategoryView.as_view(), name="delete_store_category"),
    path('toggle-store-category-status/<int:category_id>/', ToggleStoreCategoryStatus.as_view(), name='toggle_store_cetegory_status'),
  


# product_sub_category
    path('product_sub_category/', ManageProductSubCategoryListView.as_view(), name='manage_product_sub_category_list'),
    path("product_sub_categories/create/", ManageProductSubCategoryCreateView.as_view(), name="manage_product_sub_category_create"),
    path('product_sub_categories/<int:pk>/edit/', ManageProductSubCategoryEditView.as_view(), name='manage_product_sub_category_edit'),
    path('product_sub_categories/delete/<int:pk>/', ManageProductSubCategoryDeleteView.as_view(), name='manage_product_sub_category_delete'),
    path('product_sub_category/toggle-active/<int:pk>/', ManageToggleProductSubCategoryActiveView.as_view(), name='manage_toggle_product_sub_category_active'),

    # Product URLs
    path('products/', ManageProductListView.as_view(), name='manage_product_list'),
    path("products/create/", ManageProductCreateView.as_view(), name="manage_product_create"),
    path("products/edit/<int:pk>/", ManageProductEditView.as_view(), name="manage_product_edit"),
    path("products/delete/<int:pk>/", ManageProductDeleteView.as_view(), name="manage_product_delete"),
    path('products/toggle-active/<int:pk>/', ManageToggleProductActiveView.as_view(), name='manage_toggle_product_active'),

    # Product Category URLs
    path('product_categories/', ManageProductCategoryListView.as_view(), name='manage_product_category_list'),
    path("product_categories/create/", ManageProductCategoryCreateView.as_view(), name="manage_product_category_create"),
    path("product_categories/edit/<int:pk>/", ManageProductCategoryEditView.as_view(), name="manage_product_category_edit"),
    path("product_categories/delete/<int:pk>/", ManageProductCategoryDeleteView.as_view(), name="manage_product_category_delete"),
    path('product_categories/toggle-active/<int:pk>/', ManageToggleProductCategoryActiveView.as_view(), name='manage_toggle_product_category_active'),



    #store urls by priya
    # path('stores/', ManageStoreView.as_view(), name='manage_Store_list'),
    # path('stores/create/', ManageCreateStore.as_view(), name='manage_create_store'),
    # path('stores/update/<int:pk>/', ManageUpdateStoreView.as_view(), name='manage_update_store'),
    # path('toggle-store-status/<int:store_id>/', ToggleStoreStatus.as_view(), name='toggle_store_status'),
    

    #store urls by rahul
    path('stores/', ManageStoreListView.as_view(), name='manage_Store_list'),
    path('stores/create/', ManageCreateStoreView.as_view(), name='manage_create_store'),
    path('stores/update/<int:pk>/', ManageUpdateStoreView.as_view(), name='manage_update_store'),
    path('toggle-store-status/<int:store_id>/', ToggleStoreStatus.as_view(), name='toggle_store_status'),


    #store category url
    path('stores/category/', ManageStoreCategoryView.as_view(), name='manage_Store_category_list'),
    path('store-category/create/', ManageCreateStoreCategoryView.as_view(), name='manage_create_store_category'),
    path("store-category/delete/<int:category_id>/", ManageDeleteStoreCategoryView.as_view(), name="delete_store_category"),
    path('toggle-store-category-status/<int:category_id>/', ToggleStoreCategoryStatus.as_view(), name='toggle_store_cetegory_status'),

    path('stores/category/update/<int:pk>/',ManageCategoryUpdateStoreView.as_view(), name='manage_update_store_category'),


    


    path('templates/', ManageTemplateListView.as_view(), name='manage_template_list'),
    path('templates/create/', ManageTemplateCreateView.as_view(), name='manage_template_create'),
    path("templates/edit/<int:pk>/", ManageTemplateEditView.as_view(), name="manage_template_edit"),
    path('templates/delete/<int:pk>/', ManageTemplateDeleteView.as_view(), name='manage_template_delete'),
    path("templates/<int:pk>/toggle/", ManageToggletemplatesActiveView.as_view(), name="manage_toggle_template_active"),

]
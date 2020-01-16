from django.contrib import admin
from coupon.models import Coupon

class couponInline(admin.TabularInline):
    model = Coupon

class MyAdminSite(admin.AdminSite):
    site_header = 'Coupon Managment System'
    site_title = 'Coupon'

admin_site = MyAdminSite(name='management')

@admin.register(Coupon)
class couponAdmin(admin.ModelAdmin):
    #all the info show to user
    list_display =('name','discount','value','modified_by','modified_at','created_at','state','CouponCode')

    ordering = ('created_at',)

    list_editable = ['discount', 'modified_at','state']

    date_hierarchy = 'created_at'

    


    # fieldsets =(
    #     ['Main',{
    #         'fields':('name','discount')
    #     }],
    #     ['Advance',{
    #         'classes':('collapse',),
    #         'fields':('value','modified_by','modified_at','state')
    #     }]
    # )

    search_fields =(
        'name',
        'discount',
        'state',
        'modefied_at',
        )

#admin.site.register(Coupon,couponAdmin)

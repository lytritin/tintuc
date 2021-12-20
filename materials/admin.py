from django.contrib import admin

# Register your models here.
from materials.models import Material


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('phieunhap', 'sohoadon', 'ngaythang', 'tenvattu')
    search_fields = ('phieunhap',)


admin.site.register(Material, MaterialAdmin)
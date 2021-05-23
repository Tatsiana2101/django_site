from django.contrib import admin
from .models import Positions, Evening, Sale, Shoes, Veil, Accessories, EveningDress, Wedding
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class WeddingAdminForm(forms.ModelForm):
    notes = forms.CharField(label="Метки", widget=CKEditorUploadingWidget())

    class Meta:
        model = Wedding
        fields = '__all__'


class WeddingAdmin(admin.ModelAdmin):
    list_display = ( "id", "name", "price", "get_image")
    readonly_fields = ("get_image", )
    list_display_links = ("name",)
    list_filter = ("type",)
    search_fields = ("name",)
    form = WeddingAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image1.url} wigth="90" height="110" ')

    get_image.short_description = "Изображение"


class EveningDressAdminForm(forms.ModelForm):
    notes = forms.CharField(label="Метки", widget=CKEditorUploadingWidget())

    class Meta:
        model = Wedding
        fields = '__all__'


class EveningDressAdmin(admin.ModelAdmin):
    list_display = ( "id", "name", "price", "get_image")
    readonly_fields = ("get_image", )
    list_display_links = ("name",)
    list_filter = ("type",)
    search_fields = ("name",)
    form = WeddingAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image1.url} wigth="90" height="110" ')

    get_image.short_description = "Изображение"


class SaleAdminForm(forms.ModelForm):
    notes = forms.CharField(label="Метки", widget=CKEditorUploadingWidget())

    class Meta:
        model = Wedding
        fields = '__all__'


class SaleAdmin(admin.ModelAdmin):
    list_display = ( "id", "name", "price", "get_image")
    readonly_fields = ("get_image", )
    list_display_links = ("name",)
    search_fields = ("name",)
    form = WeddingAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image1.url} wigth="90" height="110" ')

    get_image.short_description = "Изображение"


class ShoesAdminForm(forms.ModelForm):
    notes = forms.CharField(label="Метки", widget=CKEditorUploadingWidget())

    class Meta:
        model = Wedding
        fields = '__all__'


class ShoesAdmin(admin.ModelAdmin):
    list_display = ( "id", "name", "price", "get_image")
    readonly_fields = ("get_image", )
    list_display_links = ("name",)
    list_filter = ("type",)
    search_fields = ("name",)
    form = WeddingAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image1.url} wigth="90" height="110" ')

    get_image.short_description = "Изображение"


class VeilAdminForm(forms.ModelForm):
    notes = forms.CharField(label="Метки", widget=CKEditorUploadingWidget())

    class Meta:
        model = Wedding
        fields = '__all__'


class VeilAdmin(admin.ModelAdmin):
    list_display = ( "id", "name", "price", "get_image")
    readonly_fields = ("get_image", )
    list_display_links = ("name",)
    list_filter = ("type",)
    search_fields = ("name",)
    form = WeddingAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image1.url} wigth="90" height="110" ')

    get_image.short_description = "Изображение"


class AccessoriesAdminForm(forms.ModelForm):
    notes = forms.CharField(label="Метки", widget=CKEditorUploadingWidget())

    class Meta:
        model = Wedding
        fields = '__all__'


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ( "id", "name", "price", "get_image")
    readonly_fields = ("get_image", )
    list_display_links = ("name",)
    list_filter = ("type",)
    search_fields = ("name",)
    form = WeddingAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image1.url} wigth="90" height="110" ')

    get_image.short_description = "Изображение"




admin.site.register(Wedding, WeddingAdmin)
admin.site.register(EveningDress, EveningDressAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Veil, VeilAdmin)
admin.site.register(Accessories, AccessoriesAdmin)

admin.site.site_title = "Панель администратора NICOLE"
admin.site.site_header = "Панель администратора NICOLE"


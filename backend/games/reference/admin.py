from django.contrib import admin
from .models import Language, ProductLanguage, Ganre, SubGanre

class GanreAdmin(admin.ModelAdmin):
    pass
        
class SubGanreAdmin (admin.ModelAdmin):
    pass

class LanguageAdmin(admin.ModelAdmin):
    pass


class ProductLanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.register(ProductLanguage, ProductLanguageAdmin)
admin.site.register(Ganre, GanreAdmin)
admin.site.register(SubGanre, SubGanreAdmin)

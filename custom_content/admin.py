from .models import PlainText
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register


class PlainTextAdmin(ModelAdmin):
    """Plain Text wagtail admin."""

    model = PlainText
    menu_label = "Plain Text"  # ditch this to use verbose_name_plural from model
    menu_icon = "doc-empty"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        True  # or True to exclude pages of this type from Wagtail's explorer view
    )
    list_display = ("plain_text",)  # adds a filter to the modeladmin page
    list_filter = ("plain_text",)
    search_fields = ("plain_text",)


modeladmin_register(PlainTextAdmin)

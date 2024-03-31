from django.contrib import admin

from .models import *


class AdminPost(admin.ModelAdmin):
    list_display = ["title", "date_posted", "author"]
    actions = ["custom_action"]  # Registering the custom action
    search_fields = ["title", "content"]
    list_filter = ["title", "date_posted", "author"]
    readonly_field = ["date_posted"]

    def custom_action(self, request, queryset):
        # Define the logic for your custom action here
        # 'request' is the current request object, and 'queryset' is the selected objects
        queryset.update(
            status="published"
        )  # Example: Update the 'status' field to 'published' for selected objects
        self.message_user(
            request, "Selected items updated successfully."
        )  # Display a success message

    custom_action.short_description = (
        "Custom Action"  # Set the display name for the custom action
    )


admin.site.register(Post, AdminPost)

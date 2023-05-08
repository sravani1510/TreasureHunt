# from django.contrib import admin

# # Register your models here.
from .models import TreasureHunt

# admin.site.register(TreasureHunt)
import os

from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse


class TreasureHuntAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'answer')

    actions = ['export_data']

    def export_data(self, request, queryset):
        # Create a folder for each user
        for user in queryset.values_list('user__username', flat=True).distinct():
            folder_name = f"{user}_data"
            folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Save data for each level in a separate file inside the user folder
            for level in range(1, 9):
                level_data = queryset.filter(user__username=user, level=level).values_list('answer', flat=True)
                file_path = os.path.join(folder_path, f"level{level}.txt")
                with open(file_path, 'w') as f:
                    f.write('\n'.join(level_data))

        self.message_user(request, "Data exported successfully.")

    export_data.short_description = "Export data for selected rows"

admin.site.register(TreasureHunt, TreasureHuntAdmin)
# admin.site.register(UserAnswer)
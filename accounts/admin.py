from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, PtoHistory

# Prepare the profile model to be appended to the end of the user model for easier viewing in the django admin.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# Override the default django admin user model to include the profile.
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# Models need to be registered in order to show up in the django admin.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(PtoHistory)

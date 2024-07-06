from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile, Genre, Show, Episode, Movie, Review, SubscriptionType, Subscription, ViewingHistory, Watchlist

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email','is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None,{
         'classes': ('wide',),
         'fields': ('username', 'email', 'pass', 'password2', 'is_staff', 'is_active')
        }
         ),
    )
    search_fields = ('username', 'email')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Genre)
admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(SubscriptionType)
admin.site.register(Subscription)
admin.site.register(ViewingHistory)
admin.site.register(Watchlist)





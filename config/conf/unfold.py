# from django.templatetags.static import static
# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse_lazy
from . import navigation

UNFOLD = {
    "DASHBOARD_CALLBACK": "core.http.views.dashboard_callback",
    "SITE_TITLE": None,
    "SITE_HEADER": None,
    "SITE_URL": "/",
    # "SITE_ICON": {
    # "light": lambda request: static("icon-light.svg"),  # light mode
    # "dark": lambda request: static("icon-dark.svg"),  # dark mode
    # },
    # "SITE_LOGO": {
    # "light": lambda request: static("logo-light.svg"),  # light mode
    # "dark": lambda request: static("logo-dark.svg"),  # dark mode
    # },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,
    # "THEME": "dark",
    # "STYLES": [
    # lambda request: static("css/style.css"),
    # ],
    # "SCRIPTS": [
    # lambda request: static("js/script.js"),
    # ],
    "COLORS": {
        "primary": {
            "50": "220 255 230",
            "100": "190 255 200",
            "200": "160 255 170",
            "300": "130 255 140",
            "400": "100 255 110",
            "500": "70 255 80",
            "600": "50 225 70",
            "700": "40 195 60",
            "800": "30 165 50",
            "900": "20 135 40",
            "950": "10 105 30",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "uz": "🇺🇿",
                "ru": "🇷🇺",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,
        "navigation": navigation.PAGES,
    },
}

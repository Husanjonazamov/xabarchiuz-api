from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Users"),
                "icon": "group",
                "link": reverse_lazy("admin:http_user_changelist"),
            },
            {
                "title": _("Group"),
                "icon": "group",
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
    {
        "title": _("Arcticle"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Article"),
                "icon": "article",
                "link": reverse_lazy("admin:arcticle_article_changelist")
            },
            {
                "title": _("Category"),
                "icon": "category",
                "link": reverse_lazy("admin:arcticle_category_changelist")
            },
            {
                "title": _("Tags"),
                "icon": "loyalty",
                "link": reverse_lazy("admin:arcticle_tag_changelist")
            },
            {
                "title": _("ArticleSection"),
                "icon": "subject",
                "link": reverse_lazy("admin:arcticle_articlesection_changelist")
            },
        ],
    },
]

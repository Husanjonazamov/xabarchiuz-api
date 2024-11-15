from django.contrib import admin
from core.apps.arcticle.models.models import Article, Category, Tag, ArticleSection
from django.utils.html import format_html




class ArticleSectionInline(admin.TabularInline):  # Yoki admin.StackedInline
    model = ArticleSection
    extra = 1  # Yana qanchta bo'sh maydon ko'rsatish kerak


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'display_basic_image', 'is_published', 'published_date', 'display_tags')
    search_fields = ('title', 'slug', 'category__name')  
    list_filter = ('category', 'is_published', 'tags')  
    prepopulated_fields = {"slug": ("title",)}  
    ordering = ('-published_date',)  
    inlines = [ArticleSectionInline]  # ArticleSection inline qo'shish
    

    def display_basic_image(self, obj):
        if obj.basic_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.basic_image.url)
        return "No Image"

    display_basic_image.short_description = 'Basic Image' 

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    display_tags.short_description = 'Tags' 





admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ArticleSection)


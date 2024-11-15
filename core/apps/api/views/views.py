from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView
from core.apps.api.serializers.serializers import ArticleSerializer, ArticleDetailSerializer, CategorySerializer, \
    CategoryArticleSerializer
from core.apps.arcticle.models.models import Article, Category
from django.db.models import Q





class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        
        tag_name = self.request.query_params.get('tag')  
        
        if tag_name:
            print(f"Filtering by tag: {tag_name}") 
            queryset = queryset.filter(tags__name__iexact=tag_name)
        
        
        print(f"Final queryset: {queryset}")  
        
        return queryset





class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Article.objects.filter(slug=slug)



class ArticleSearchView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)  # 'q' parametrini olish
        if query:
            return Article.objects.filter(
                Q(title__icontains=query) | Q(slug__icontains=query)
            ).distinct()  # Dublikatlarni oldini olish uchun distinct() qo‘llandi
        else:
            return Article.objects.none()




class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryArticleView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryArticleSerializer
    lookup_field = 'name'

    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(Category, name__iexact=name)

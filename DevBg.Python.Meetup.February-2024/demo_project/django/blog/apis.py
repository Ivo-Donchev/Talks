from rest_framework import generics, serializers
from .models import Article, Comment, Reaction


class ArticleDetaiApiView(generics.RetrieveAPIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ["id", "title", "content", "author"]

    queryset = Article.objects.all()
    serializer_class = OutputSerializer


class CommentListApiView(generics.ListAPIView):
    class OutputSerializer(serializers.ModelSerializer):
        reactions_count = serializers.SerializerMethodField()

        class Meta:
            model = Comment
            fields = [
                "id",
                "article",
                "author",
                "content",
                "created_at",
                "reactions_count",
            ]

        def get_reactions_count(self, obj):
            return Reaction.objects.filter(comment=obj).count()

    serializer_class = OutputSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned comments to a given article,
        by filtering against a `article` query parameter in the URL.
        """
        article_id = self.kwargs["pk"]
        return Comment.objects.filter(article_id=article_id)

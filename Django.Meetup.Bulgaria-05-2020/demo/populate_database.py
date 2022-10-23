from dashboard.models import Author, Article


def populate():
    print('Populating with 1000 authors')

    for i in range(1000, 10000):
        Author.objects.create(
            name=f'Author {i}',
            age=i,
            author_field_1=f'author_field_1_{i}',
            author_field_2=f'author_field_2_{i}',
            author_field_3=f'author_field_3_{i}',
            author_field_4=f'author_field_4_{i}',
            author_field_5=f'author_field_5_{i}',
            author_field_6=f'author_field_6_{i}',
            author_field_7=f'author_field_7_{i}',
            author_field_8=f'author_field_8_{i}',
            author_field_9=f'author_field_9_{i}',
            author_field_10=f'author_field_10_{i}',
            author_field_11=f'author_field_11_{i}',
            author_field_12=f'author_field_12_{i}',
            author_field_13=f'author_field_13_{i}',
            author_field_14=f'author_field_14_{i}',
            author_field_15=f'author_field_15_{i}',
            author_field_16=f'author_field_16_{i}',
            author_field_17=f'author_field_17_{i}',
            author_field_18=f'author_field_18_{i}',
            author_field_19=f'author_field_19_{i}',
            author_field_20=f'author_field_20_{i}',
            author_field_21=f'author_field_21_{i}',
            author_field_22=f'author_field_22_{i}',
            author_field_23=f'author_field_23_{i}',
            author_field_24=f'author_field_24_{i}',
            author_field_25=f'author_field_25_{i}',
            author_field_26=f'author_field_26_{i}',
            author_field_27=f'author_field_27_{i}',
            author_field_28=f'author_field_28_{i}',
            author_field_29=f'author_field_29_{i}',
            author_field_30=f'author_field_30_{i}',
        )

    print('Populating with 2000 articles')

    authors = list(Author.objects.all())

    for i in range(2000, 10000):
        Article.objects.create(
            title=f'Title {i}',
            content='Very very long content here .....',
            author=authors[1000 - 1000 // (i + 1)],
            article_field_1=f'article_field_1_{i}',
            article_field_2=f'article_field_2_{i}',
            article_field_3=f'article_field_3_{i}',
            article_field_4=f'article_field_4_{i}',
            article_field_5=f'article_field_5_{i}',
            article_field_6=f'article_field_6_{i}',
            article_field_7=f'article_field_7_{i}',
            article_field_8=f'article_field_8_{i}',
            article_field_9=f'article_field_9_{i}',
            article_field_10=f'article_field_10_{i}',
            article_field_11=f'article_field_11_{i}',
            article_field_12=f'article_field_12_{i}',
            article_field_13=f'article_field_13_{i}',
            article_field_14=f'article_field_14_{i}',
            article_field_15=f'article_field_15_{i}',
            article_field_16=f'article_field_16_{i}',
            article_field_17=f'article_field_17_{i}',
            article_field_18=f'article_field_18_{i}',
            article_field_19=f'article_field_19_{i}',
            article_field_20=f'article_field_20_{i}',
            article_field_21=f'article_field_21_{i}',
            article_field_22=f'article_field_22_{i}',
            article_field_23=f'article_field_23_{i}',
            article_field_24=f'article_field_24_{i}',
            article_field_25=f'article_field_25_{i}',
            article_field_26=f'article_field_26_{i}',
            article_field_27=f'article_field_27_{i}',
            article_field_28=f'article_field_28_{i}',
            article_field_29=f'article_field_29_{i}',
            article_field_30=f'article_field_30_{i}',
        )

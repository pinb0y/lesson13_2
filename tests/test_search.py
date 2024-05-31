from src.artice import Article


def test_search_3(list_articles):
    """Тестирование поиска статьи по id"""
    searchable_article: Article = Article.search(3)
    assert searchable_article.title == "test3"


def test_search_4(list_articles):
    """Тестирование поиска статьи по id"""
    searchable_article: Article = Article.search(4)
    assert searchable_article.title == "test4"

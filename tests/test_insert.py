from src.artice import Article


def test_insert(one_article):
    """Тест для проверки метода insert"""
    assert len(Article.articles) == 1


def test_article_id(one_article):
    """Тест на проверку установки id статьи"""
    assert one_article.article_id == 1


def test_increase_articles(two_articles):
    """Тест на проверку увеличения id статьи"""
    assert two_articles.article_id == 2


def test_increase_article_count(two_articles):
    """Тест на проверку увеличение списка статей"""
    assert len(Article.articles) == 2

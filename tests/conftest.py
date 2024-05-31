import pytest

from src.artice import Article


@pytest.fixture
def one_article():
    Article.articles = dict()
    return Article.insert("test", "test test")


@pytest.fixture
def two_articles():
    Article.articles = dict()
    Article.insert("test", "test test")
    return Article.insert("test", "test test")

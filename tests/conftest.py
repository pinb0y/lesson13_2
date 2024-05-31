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


@pytest.fixture
def list_articles():
    Article.articles = dict()
    Article.insert("test1", "test1 test")
    Article.insert("test2", "test2 test")
    Article.insert("test3", "test3 test")
    Article.insert("test4", "test4 test")
    Article.insert("test5", "test5 test")
    return Article.insert("test6", "test6 test")

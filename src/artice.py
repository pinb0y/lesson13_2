class Article:
    """Класс для хранения статей"""
    article_id: int
    title: str
    content: str

    articles = dict()  # атрибут на уровне класса для хранения всех статей

    def __init__(self, title, content):
        self.article_id = self.get_new_id()
        self.title = title
        self.content = content

    def get_new_id(self) -> int:
        """Метод получения след айди статьи"""
        return len(self.articles) + 1

    @classmethod
    def insert(cls, title: str, content: str):
        """Метод для создания и добавления статьи"""
        new_article = cls(title, content)
        cls.articles[new_article.article_id] = new_article
        return new_article


if __name__ == "__main__":
    new_article1 = Article.insert("test", "test test test")
    print(new_article1.article_id)
    new_article2 = Article.insert("test2", "test test test2")
    print(new_article2.article_id)

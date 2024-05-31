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

    @classmethod
    def search(cls, article_id):
        """Метод для поиска статьи"""
        # return cls(1, 1)
        return cls.articles[article_id]



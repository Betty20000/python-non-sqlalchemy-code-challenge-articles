
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters long")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        return [author for author, count in author_count.items() if count > 2] or None


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters long")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.articles().append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot change the title of the article")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        author = Author("Carry Bradshaw")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        magazine = Magazine("Vogue", "Fashion")

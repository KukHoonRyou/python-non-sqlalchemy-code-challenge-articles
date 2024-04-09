class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title (self):
        return self._title
    
    @title.setter
    def title (self, title):
        if isinstance(title, str) and not hasattr(self, "title") and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception("Invalid title value")

    @property
    def article (self):
        return self._article
    
    @article.setter
    def article (self, article):
        if isinstance(article, Article):
            self._article = article
        else:
            raise Exception("Invalid article value")
    
    @property
    def magazine (self):
        return self._magazine
    
    @magazine.setter
    def magazine (self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("Invalid magazine value")
        
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and 0 < len(name):
            self._name = name
        else:
            raise Exception("Invalid name value")

    def articles(self):
        return[article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for article in self.articles() for magazine in [article.magazine]))

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)
    
    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Invalid name value")

    @property
    def category (self):
        return self._category
    
    @category.setter
    def category (self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category = category
        else:
            raise Exception("Invalid category value")

    def articles(self):
        return[article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all or all(len(magazine.articles()) == 0 for magazine in cls.all):
            return None
        return max(cls.all, key = lambda magazine: len(magazine.articles()))
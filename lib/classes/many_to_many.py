class Article: 

    all = [] # class variable for storing all instances of Article

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self) # add current instance to the "all" list of Article

    @property
    def title (self):
        return self._title
    
    @title.setter
    def title (self, title):
        if isinstance(title, str) and not hasattr(self, "title") and 5 <= len(title) <= 50: # title must be string and not be able to change and between 5 and 50 characters long
            self._title = title
        else:
            raise Exception("Invalid title value") # raise exception when value invalid
    @property
    def article (self):
        return self._article
    
    @article.setter
    def article (self, article):
        if isinstance(article, Article):
            self._article = article
        else:
            raise Exception("Invalid article value") # raise exception when value invalid
    
    @property
    def magazine (self):
        return self._magazine
    
    @magazine.setter
    def magazine (self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("Invalid magazine value") # raise exception when value invalid
        
class Author:

    all = [] # class variable for storing all instances of Author

    def __init__(self, name): # Author is initialized with a name
        self.name = name
        type(self).all.append(self) # add current instance to the "all" list of Author

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and 0 < len(name): # name is type of string, not be able to change(hasattr()), and length is longer than 0 character
            self._name = name
        else:
            raise Exception("Invalid name value") # raise exception when value invalid

    def articles(self):
        return[article for article in Article.all if article.author is self] # return all article written by author

    def magazines(self):
        return list({article.magazine for article in self.articles()}) # return a unique list of magazines that contain the author's articles

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title) # create a new article instance
        return new_article # return the new article instance

    def topic_areas(self):
        if not self.articles():
            return None #if the author has no articles, return None
        return list(set(magazine.category for article in self.articles() for magazine in [article.magazine])) # return a list of categories of magazines containing the author's articles

class Magazine:

    all = [] # class variable for storing all instances of Magazine

    def __init__(self, name, category):
        self.name = name # initialize magazine name
        self.category = category #initialize magazine category 
        type(self).all.append(self) # add current instance to the "all" list of Magazine
    
    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16: # name must be string and between 2 and 16 characters long
            self._name = name
        else:
            raise Exception("Invalid name value") # raise exception when value invalid

    @property
    def category (self):
        return self._category
    
    @category.setter
    def category (self, category):
        if isinstance(category, str) and 0 < len(category): # category must be string and longer than 0 character
            self._category = category
        else:
            raise Exception("Invalid category value") # raise exception when value invalid

    def articles(self):
        return[article for article in Article.all if article.magazine is self] # return all articles published in this magazine

    def contributors(self):
        return list({article.author for article in self.articles()}) # return a unique list of authors who contributed to this magazine

    def article_titles(self):
        titles = [article.title for article in self.articles()] # return the titles of all articles published in this magazine
        return titles if titles else None # if any, return the list of titles, or if not, return None

    def contributing_authors(self):
        author_counts = {} # initialize a dictionary to store the count of contributions for each author
        for article in self.articles(): #loop all articles published
            if article.author in author_counts: # if author has article already in author_counts, 
                author_counts[article.author] += 1 # increase the count 1
            else:
                author_counts[article.author] = 1 # if not, add the new author to author_counts with count 1
        authors = [author for author, count in author_counts.items() if count > 2] # filter authors in author_counts who has more than 2 counts
        return authors if authors else None # return the list, if not return None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all or all(len(magazine.articles()) == 0 for magazine in cls.all):
            return None # return None if there is no magazine or all magazine have no article
        def article_count(magazine):
            return len(magazine.articles()) # number of article published in the magazine
        
        return max(cls.all, key = article_count) # return the magazine withe the most article published
    
    # can use lambda, but I don't, because I want show the processes

    # @classmethod
    # def top_publisher(cls):
    #     if not cls.all or all(len(magazine.articles()) == 0 for magazine in cls.all):
    #         return None
    #     return max(cls.all, key = lambda magazine: len(magazine.articles()))
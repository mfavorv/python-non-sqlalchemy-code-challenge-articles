class Article:
    all = []
    def __init__(self, author, magazine, title = "How to wear a tutu with style"):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, title):
        if not hasattr(self, "_name"):
         if((type(title) == str) and (5<= len(title) <=50)):
                self._title = title
         else:
             raise ValueError("Title must be a string with length between 5 and 50 characters")              
        else:
            print("Article already set.")             

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
       if isinstance(author, Author):
           self._author = author
       else:
           raise ValueError("author must be an instance of Author")


    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
       if isinstance(magazine, Magazine):
            self._magazine = magazine
       else:
           raise ValueError("Magazine must be an instance of Magazine")


class Author:
    def __init__(self, name):
        self.name = name
               
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not hasattr(self, "_name"):
         if((type(name) == str) and len(name) > 0):
             self._name = name
         else:
            print("Name must be a string and have at least one character")
        else:
            print("Name has already been set.")
        
    def articles(self):
          articles = []
          for article in Article.all:
              if article.author == self:
                  if isinstance (article, Article):
                      articles.append(article)
          return articles
    pass

    def magazines(self):
      magazines = set()
      for article in Article.all:
        if article.author == self and isinstance(article.magazine, Magazine):
            magazines.add(article.magazine)
      return list(magazines)
    pass

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
          article = Article(self, magazine, title)
          return article
        else:
            raise ValueError("The magazine must be an instance of Magazine.")
        pass

    def topic_areas(self):
      categories = set()
      magazines = []
      for article in Article.all:
        if article.author == self and isinstance(article.magazine, Magazine):
              magazines.append(article.magazine)
      for m in magazines:
        categories.add(m.category)
      categories = list(categories)

      if len(categories) > 0:
        return categories
      else:
        None
           
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
       
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
     if isinstance(name, str):
        if len(name) <=16 and len(name) >=2:
            self._name = name
        else:
            raise ValueError("Name does not have between 2 and 16 characters")
     else:
        raise ValueError("Name is not a string .")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str):
            if len(category) > 0:
                self._category = category
            else:
                raise ValueError("Category must not be an empty string")
        else:
            raise ValueError("Category must be a string")

    def articles(self):
        articles =[]
        for article in Article.all:
            if article.magazine == self and isinstance(article, Article):
                articles.append(article)
        return articles
        pass

    def contributors(self):
      authors = set()
      for article in Article.all:
        if article.magazine == self and isinstance(article.author, Author):
            authors.add(article.author)
      return list(authors)
    pass
    

    def article_titles(self):
        titles = []
        for article in Article.all:
            if article.magazine == self:
              titles.append(article.title)
        if len(titles) > 0:
            return titles
        else:
            return None
        pass

    def contributing_authors(self):
        excellent_authors = []
        authors = []
        for article in Article.all:
            if article.magazine == self and isinstance(article.author, Author):
                authors.append(article.author)
        
        author_counts = {}
        for author in authors:
            author_counts[author] = author_counts.get(author, 0) + 1
        
        for author, count in author_counts.items():
            if count > 2:
                excellent_authors.append(author)

            if len(excellent_authors) > 0:
                return excellent_authors
            else:
                return None
            pass

    @classmethod
    def top_publisher(cls):
        magazine_counts = {}
        maximum = 0
        top_magazine = None

        for article in Article.all:
            magazine_counts[article.magazine] = magazine_counts.get(article.magazine, 0) + 1

        for m, count in magazine_counts.items():
            if count > maximum:
                maximum = count
                top_magazine = m

        return top_magazine

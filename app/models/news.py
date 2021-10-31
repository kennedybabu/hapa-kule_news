class News:
    '''
    News class to define News object
    '''

    def __init__(self, title, description, image, author, date_created, link):
        self.title = title
        self.description = description
        self.image = 'https://image.tmdb.org/t/p/w500/' + image
        self.author = author
        self.date_created = date_created
        self.link = link
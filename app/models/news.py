class News:
    '''
    News class to define News object
    '''

    def __init__(self, id, description, image, author, date_created):
        self.id = id
        self.description = description
        self.image = 'https://image.tmdb.org/t/p/w500/' + image
        self.author = author
        self.date_created = date_created
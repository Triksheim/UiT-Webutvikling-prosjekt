class Content:

    def __init__(self,contentID, code, title, description, date, tags, filename, mimetype, size, restriction, views, user, likes):
        self.contentID = contentID
        self.code = code
        self.title = title
        self.description = description
        self.date = date.strftime('%Y-%m-%d')
        self.tags = tags
        self.filename = filename
        self.mimetype = mimetype
        self.size = size
        self.restriction = restriction
        self.views = views
        self.user_username = user
        self.likes = likes
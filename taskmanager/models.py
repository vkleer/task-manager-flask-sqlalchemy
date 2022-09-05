from taskmanager import db


class Category(db.Model):
    # Schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        # __rept__ to represent itself in the form of a string
        return self


class Task(db.Model):
    # Schema for the Task model
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        # __rept__ to represent itself in the form of a string
        return self

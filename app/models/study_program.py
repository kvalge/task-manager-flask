from app.extensions import db


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    organization = db.Column(db.String(150))
    description = db.Column(db.String(2500))

    def __repr__(self):
        return f'<Study program "{self.title}">'
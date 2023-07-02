from app.extensions import db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.String(2500))

    def __repr__(self):
        return f'<Job "{self.title}">'

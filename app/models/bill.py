from app.extensions import db


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(1500))
    period = db.Column(db.String(150))
    price = db.Column(db.Numeric(precision=2))

    def __repr__(self):
        return f'<Job "{self.title}">'
from app import db


# Объект, хранящий в себе все данные об URL и её коротком аналоге, генерирующемся в приложении
class UrlData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000), index=True, unique=True)
    short_url = db.Column(db.String(30), index=True, unique=True)

    def __repr__(self):
        return f'<UrlData: id={self.id}, url={self.url}, short_url={self.short_url}>'


# Срезы строки, по которым генерируются короткие URL
class Slices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    s1 = db.Column(db.Integer, index=True)
    s2 = db.Column(db.Integer, index=True)
    s3 = db.Column(db.Integer, index=True)
    s4 = db.Column(db.Integer, index=True)
    s5 = db.Column(db.Integer, index=True)
    s6 = db.Column(db.Integer, index=True)

    def __repr__(self):
        return f'<Slices: s1={self.s1}, s2={self.s2}, s3={self.s3}, s4={self.s4}, s5={self.s5}, s6={self.s6}>'

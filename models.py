FROM flask_sqlalchemy IMPORT SQLAlchemy
db= SQLAlchemy()

DEFAULT_IMAGE_URL = "https://tinyurl.com/truffle-cupcake"

def connect_db(app):
    """ Connects to database """

    db.app = app
    db.init_app(app)

def Cupcake(db.Models):
    """model for cupcakes"""

    __tablename__ = "cupcakes"

    id = db.Columne(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullalbe=False)
    rating = db.Column(db.Float, nullalbe=False)
    image = db.Column(db.String(300), default=DEFAULT_IMAGE_URL)
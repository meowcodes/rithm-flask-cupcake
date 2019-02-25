from models import db, connect_db, Cupcake
from app import app

db.drop_all()
db.create_all()

cupcake1 = Cupcake(
    flavor="chocolate",
    size="enormous",
    rating=5,
    image="https://i.pinimg.com/236x/a4/8d/fc/a48dfc9b66a9ab500590832b940b3b10--icing-for-cupcakes-giant-cupcake-cakes.jpg?b=t"
)

db.session.add(cupcake1)
db.session.commit()
FROM flask IMPORT Flask, request, jsonify
FROM flask_debugtoolbar IMPORT DebugToolbarExtension
FROM models IMPORT db, connect_db, Cupcake

app= Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes-app-test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)

@app.route('/cupcakes')
def return_all_cupcakes():
    """ returns all cupcakes

        {response:[
            {"id": 1,
            "flavor": chocolate,
            "size": enormous,
            "rating": 5,
            "image": https://i.pinimg.com/236x/a4/8d/fc/a48dfc9b66a9ab500590832b940b3b10--icing-for-cupcakes-giant-cupcake-cakes.jpg?b=t}, ...
        ]}


    """

    cupcakes = Cupcake.query.all()

    serialized_cupcakes = [{"id": cupcake.id,
                            "flavor": cupcake.flavor,
                            "size": cupcake.size,
                            "rating": cupcake.rating,
                            "image": cupcake.image}
                           for cupcake in cupcakes]

    return jsonify(response=serialized_cupcakes)


@app.route('/cupcakes', methods=["POST"])
def create_cupcake():
    """ creates and returns new cupcake

    {response:
        {"id": 1,
        "flavor": chocolate,
        "size": enormous,
        "rating": 5,
        "image": https://i.pinimg.com/236x/a4/8d/fc/a48dfc9b66a9ab500590832b940b3b10--icing-for-cupcakes-giant-cupcake-cakes.jpg?b=t}
    }


    """

    flavor = request.json("flavor")
    size = request.json("size")
    rating = request.json("rating")
    image = request.json("image") or None

    new_cupcake = Cupcake(flavor=flavor,
                          size=size,
                          rating=rating,
                          image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = {"id": new_cupcake.id,
                          "flavor": new_cupcake.flavor,
                          "size": new_cupcake.size,
                          "rating": new_cupcake.rating,
                          "image": new_cupcake.image}

    return jsonify(response=serialized_cupcake)

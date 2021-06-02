
# un controlador es el comportamiento que va a tener mi API cuando
# /postres GET => mostrar los postres


from flask_restful import Resource, reqparse
from models.postre import PostreModel

# serializer (serializador)
serializerPostres = reqparse.RequestParser(bundle_errors=True)
serializerPostres.add_argument(
    "nombre", # nombre del atributio en el body
    type=str, # tipo de dato que me tiene que mandar
    required=True, # si es de caracter obligatorio o no
    help="Falta el nombre", # mensaje de ayuda en el caso fuese obligatorio y no me lo mandase
    location ="json" # en que parte del request me mandara, ta sea json (body)o url
)

serializerPostres.add_argument(
    "porcion",
    type=str,
    required=True,
    help="Falta la porcion",
    location="json"
)

class PostresController (Resource):
    def get(self):
        # SELECT * FROM postres;
        print(PostreModel.query.all())
        return "ok"


    def post(self):
        data = serializerPostres.parse_args()
        print(data)
        return "ok"

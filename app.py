from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema


class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'


schema = Schema(query=Query)

app = Flask(__name__)
view = GraphQLView.as_view('graphql', schema=schema, graphiql=True, batch=True)
app.add_url_rule('/graphql', view_func=view)


if __name__ == '__main__':
    app.run()
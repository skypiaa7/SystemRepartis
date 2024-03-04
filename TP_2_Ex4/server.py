from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

@dispatcher.add_method
def calcul(expression):
    return eval(expression)

@Request.application
def application(request):

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')

if __name__ == '__main__':
    run_simple('localhost', 8000, application)




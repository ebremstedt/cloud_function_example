import functions_framework
from requests import Request


@functions_framework.http
def main(request: Request):
    ##
    return 'Massive success!', 200

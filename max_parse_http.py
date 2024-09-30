message = {
    'Method': '', #http reqest method
    'URL': '',    #URL
    'Version': '',
    'Headers': {}, #словник всіх заголовків з відповідними іменами і значеннями
    'Body': '' #raw body srting
    }

def max_parse_http(rawhttp: str) -> dict:
    pass

print(max_parse_http("""
POST /user/create/json HTTP/1.1
Accept: application/json
Content-Type: application/json
Content-Length: 28
Host: codegym.cc
    
{
    "Id": 12345,
    "User": "John"
}
"""))
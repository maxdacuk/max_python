def max_parse_http(rawhttp: str) -> dict:
    sections = rawhttp.split('\r\n\r\n')
    header_section = sections[0]  # Заголовки та перший рядок запиту
    body = sections[1].strip() if len(sections) > 1 else ''  # Тіло запиту

    lines = header_section.split('\r\n')

    request_line = lines[0].split()
    method = request_line[0]
    url = request_line[1]
    version = request_line[2]

    headers = {}
    for line in lines[1:]:
        key, value = line.split(': ', 1)
        headers[key] = value

    # Формуємо словник для результату
    message = {
        'Method': method,
        'URL': url,
        'Version': version,
        'Headers': headers,
        'Body': body
    }
    
    return message

print(max_parse_http("""
POST /user/create/json HTTP/1.1\r\n
Accept: application/json\r\n
Content-Type: application/json\r\n
Content-Length: 28\r\n
Host: codegym.cc\r\n\r\n
{
    "Id": 12345,
    "User": "John"
}
"""))
#!/usr/bin/python3
import socket
import cgi
from json import dumps

# Get Socket to investigate Pod address and hostname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
h = socket.gethostname()

# Check if Get query type is HTML or JSON
form = cgi.FieldStorage()
if "query" not in form or form["query"].value is "html":

    color_seed = int(ip.split('.')[3]) % 6
    if color_seed is 0:
        color = '#FFA0A0'  # red
    if color_seed is 1:
        color = '#FFFFA0'  # yellow
    if color_seed is 2:
        color = '#A0FFA0'  # green
    if color_seed is 3:
        color = '#A0FFFF'  # bluegreen
    if color_seed is 4:
        color = '#A0A0FF'  # blue
    if color_seed is 5:
        color = '#FFA0FF'  # purple
    
    print("Content-Type: text/html;")
    print("")
    print("<!DOCTYPE html>")
    print("<html lang='ja'>")
    print("<head>")
    print("    <meta charset='utf-8'>")
    print("    <title>%s</title>" % ip)
    print("</head>")
    print("<body>")
    print("    <h1>NSX Solution Demo/Test Page")
    print("    <div style=\"background-color:%s;\">" % color)
    print("        <h2>IP address: %s</h2>" % ip)
    print("        <h2>Hostname: %s</h2>" % h)
    print("    </div>")
    print("</body>")
    print("</html>")

elif form["query"].value is "json":
    res = {"name":"NSX Solution Demo/Test Page", "address":ip, "hostname":h}
    print(dumps(res))

else:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Parameter:query")
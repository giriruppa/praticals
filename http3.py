import http.client

print("** This program returns a list of methods if OPTIONS is enabled **")

host = input("Enter the Host/IP: ")
port = input("Enter the Port (Default:80): ")

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', '/')
    response = connection.getresponse()
    print("Enabled Methods are: ", response.getheader('allow'))
    connection.close()

except ConnectionRefusedError:
    print("Connection Failed!")

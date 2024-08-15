import socket

# Create a socket object
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print('Socket successfully created')
except socket.error as err:
  print(f"Socket creation failed with error: {err}")
  exit()

# Set port number
port = 56789

# Bind socket to address and port
try:
  s.bind(('', port))
  print(f'Socket binded to port {port}')
except socket.error as err:
  print(f"Socket binding failed with error: {err}")
  exit()

# Listen for incoming connections
s.listen(5)
print('Socket is listening')

# Infinite loop to accept connections
while True:
  # Accept connection
  try:
    c, addr = s.accept()
    print('Got connection from', addr)
  except socket.error as err:
    print(f"Error accepting connection: {err}")
    continue

  # Send message
  message = ('Thank you for connecting').encode()
  c.send(message)

  # Close the connection
  c.close()

# Close the main socket (added after the loop)
s.close()

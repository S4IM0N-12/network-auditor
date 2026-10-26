import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn

class PortScanner:
    def __init__(self, target, ports=None, timeout=1.0, max_workers=100):
        self.target=target
        self.ports = ports or [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]
        self.timeout=timeout
        self.max_workers=max_workers
        self.results = []
        try:
            self.target_ip = socket.gethostbyname(self.target)
        except Exception:
            self.target_ip = self.target

    def _scan_port(self, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.target_ip, port))
    
                if result == 0:
                    banner = self._grab_banner(sock)
                    sock.close()
                    return {"port": port, "status": "OPEN", "banner": banner}
                sock.close()
            except Exception:
                pass
            return None

    def _grab_banner(self, sock):
        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            return banner.split('\n')[0] if banner else "Desconocido"
        except Exception:
            return "Desconocido"

    def run(self):
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            refresh_per_second=99999999
        ) as progress:
            task = progress.add_task("[cyan]Escaneando puertos...", total=len(self.ports))
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                future_to_port = {executor.submit(self._scan_port, port): port for port in self.ports}

                for future in as_completed(future_to_port):
                    result = future.result()
                    if result:
                        self.results.append(result)
                    progress.advance(task)
        return self.results    
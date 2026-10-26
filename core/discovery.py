import subprocess
import platform
import concurrent.futures

class HostDiscovey:
    def __init__(self, targets, max_workers=50):
        self.targets=targets
        self.max_workers=max_workers

    def _ping_host(self, ip):
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", "w", "1000", ip]

        try:
            result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result.returncode == 0:
                return ip
        except Exception:
            pass
        return None

    def scan_live_hosts(self):
        live_hosts = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._ping_host, ip): ip for ip in self.targets}
            for future in concurrent.futures.as_completed(futures):
                res = future.result()
                if res:
                    live_hosts.append(res)
        return live_hosts
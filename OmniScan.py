import argparse
from core.scanner import PortScanner
from utils.ui import show_banner, print_results, console
from utils.reporter import Reporter

def parse_args():
    parser = argparse.ArgumentParser(description="Escanere de Redes & Auditoria de Servicios")
    parser.add_argument("-t", "--target", required=True, help="IP o Dominio objetivo (ej: 192.168.1.1 o scanme.namp.org)")
    parser.add_argument("-p", "--ports", help="Rango o lista de puerto separados por coma (ej: 22,80,443 o 1-100)", default="top")
    parser.add_argument("-w", "--workers", type=int, default=50, help="Numero de workers (default: 50)")
    parser.add_argument("-o", "--output", help="Guardar reporte en archivo JSON (ej: reporte.json)")
    return parser.parse_args()

def parse_ports(port_arg):
    if port_arg == "top":
        return [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 3306, 3389, 5432, 8080, 8443]
    if "-" in port_arg:
        start, end = map(int, port_arg.split("-"))
        return list(range(start, end + 1))
    return list(map(int, port_arg.split(",")))

def main():
    show_banner()
    args = parse_args()
    target = args.target
    ports = parse_ports(args.ports)

    console.print(f"[bold cyan][*] Iniciando escaneo sobre:[/bold cyan] [bold white]{target}[/bold white]")
    console.print(f"[bold cyan][*] Analizando puerto:[/bold cyan] {len(ports)} | [bold cyan]Workers:[/bold cyan] {args.workers}\n")

    scanner = PortScanner(target=target, ports=ports, max_workers=args.workers)
    with console.status("[bold green]Escaneando objetivo...", spinner="dots"):
        results = scanner.run()
    print_results(target, results)
    if args.output:
        Reporter.save_json(target, results, args.output)
if __name__ == "__main__":
    main()
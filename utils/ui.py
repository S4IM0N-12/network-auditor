from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

BANNER = r"""[bold red]
  ____                 _ ____                 
 / __ \____ ___  ___  (_) __/__________ _____ 
/ /_/ / __ `__ \/ __ \/ /\ \/ ___/ __ `/ __ \
\____/_/ /_/ /_/ /_/_/_/___/\___/\__,_/_/ /_/
[/bold red]
[bold yellow] [*] Network & Port Security Scanner v1.0 [/bold yellow]
"""

def show_banner():
    console.clear()
    console.print(BANNER)

def print_results(target, results):
    table = Table(title=f"[bold cyan] Resultados de Auditoria: {target}[/bold cyan]", title_justify="center")
    table.add_column("Puerto", style="bold yellow", justify="center")
    table.add_column("Estado", style="bold green", justify="center")
    table.add_column("Banner / Servicio detectado", style="white", justify="left")
    if not results:
        console.print(Panel("[bold red]No se encontraron puerto abiertos en el objetivo.[/bold red]", border_style="red"))
        return
    for item in results:
        table.add_row(
            str(item["port"]),
            item["status"],
            item["banner"]
        )
    console.print(Panel(table, border_style="cyan"))
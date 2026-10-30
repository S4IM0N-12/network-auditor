# Network & Port Security Scanner v2.0

Herramienta de auditoría de red y escaneo de puertos desarrollada en Python. Diseñada con una arquitectura modular orientada a objetos y renderizado de resultados en tiempo real mediante interfaces profesionales con `rich`.

---

## Características Principales

* **Escaneo Multihilo (`ThreadPoolExecutor`)**: Permite analizar múltiples puertos en paralelo para reducir drásticamente el tiempo de ejecución.
* **Extracción de Banners (Banner Grabbing)**: Intenta identificar las firmas o servicios activos corriendo detrás de los puertos abiertos.
* **Arquitectura Modular**: Código separado en paquetes independientes (`core/`, `utils/`) para facilitar el mantenimiento y escalabilidad.
* **Reportes Automatizados**: Capacidad de exportar los resultados detallados de la auditoría directamente a formatos estructurados como `JSON`.

---

## Instalacion y configuracion

```bash
git clone https://github.com/S4IM0N-12/network-auditor.git
cd network-auditor/
python3 -m venv .venv
pip install -r requirements.txt
```

## USO

```bash
python3 OmniScan.py -h
Uso: python3 OmniScan.py [-h] [-t] [-p] [-w] [-o]

options:
  -h, --help            show this help message and exit
  -t, --target TARGET   IP o Dominio objetivo (ej: 192.168.1.1 o scanme.namp.org)
  -p, --ports PORTS     Rango o lista de puerto separados por coma (ej: 22,80,443 o 1-100)
  -w, --workers WORKERS
                        Numero de workers (default: 50)
  -o, --output OUTPUT   Guardar reporte en archivo JSON (ej: report.json O report.txt)

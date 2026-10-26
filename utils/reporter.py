import json
from datetime import datetime

class Reporter:
    @staticmethod
    def save_json(target, results, filename="audit_report.json"):
        data = {
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "open_ports_count": len(results),
            "details": results
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return filename
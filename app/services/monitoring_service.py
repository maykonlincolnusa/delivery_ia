def analyze_anomaly(metric: str, value: float):
    if value > 300:
        return {
            "status": "anomaly",
            "severity": "high",
            "message": f"Valor crítico detectado em {metric}"
        }

    return {
        "status": "normal",
        "severity": "low"
    }

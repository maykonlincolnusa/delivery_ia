import json
from datetime import datetime
from pathlib import Path

class S3Service:
    def save_raw_data(self, data, prefix="deliveries"):
        Path("data/raw").mkdir(parents=True, exist_ok=True)

        filename = f"data/raw/{prefix}_{datetime.utcnow().isoformat()}.json"

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        print(f"☁️ S3 simulated save: {filename}")

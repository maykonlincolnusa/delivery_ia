class EnglobaService:
    """
    Adapter / Service layer for Engloba delivery system.

    This is a MOCK implementation.
    In production, this class would handle:
    - authentication
    - API requests
    - pagination
    - error handling
    """

    def get_deliveries(self):
        # Simulated data returned from Engloba API
        return [
            {
                "delivery_id": "DEL-001",
                "courier": "Carlos",
                "route": "Zone A",
                "status": "delayed",
                "eta_minutes": 45
            },
            {
                "delivery_id": "DEL-002",
                "courier": "Ana",
                "route": "Zone B",
                "status": "on_time",
                "eta_minutes": 12
            },
            {
                "delivery_id": "DEL-003",
                "courier": "Lucas",
                "route": "Zone A",
                "status": "delayed",
                "eta_minutes": 20
            }
        ]

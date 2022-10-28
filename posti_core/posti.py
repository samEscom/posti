import requests
from typing import Optional, Dict


class Posti:

    def __init__(self):
        self._posti_session = requests.session()

    def call_request(
            self,
            method: str,
            url: str,
            params: Optional[Dict],
            json_data: Optional[Dict],
            headers: Optional[Dict]
    ) -> Dict:
        try:
            response = self._posti_session.request(
                method=method,
                url=url,
                params=params,
                json=json_data,
                headers=headers,
            )

            return {
                "status": response.status_code,
                "response": response.json(),
                "text": response.text,
            }
        except Exception as e:
            return {
                "message": str(e),
                "status": response.status_code,
                "text": response.text,
            }
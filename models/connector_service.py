"""
The Integration Layer(Extraction)
    location: models/connector_service.py
    logic: This is your "Service Class." It should not be a standard Odoo modules
        but a helper class or mixin. It handles the request library calls and manages the 
        Exponential Back-off
    Focus: Authenticating via your System Paraments (API Keys) and handling the HTTP
        lifecycle.
"""

from odoo import fields, models, api
import requests
import time
import logging

_logger = logging.getLogger(__name__)


class ConnectorService(models.Model):
    _name = 'smart.connector.service'
    _description = "Service layer for API communication"

    def _get_api_config(self):
        """Fetches API credentials from System Paraments."""
        params = self.env['ir.config_paramentr'].sudo()
        return {
            "key":params.get_params('smart.connector.api_key'),
            'url':params.get_params("smart.connector.base_url")
        }
    
    def fetch_data(self, endpoint, retries=3):
        """Fetches data with exponential back-off."""
        config = self._get_api_config()
        url = f"{config['url']/{endpoint}}"
        headers = {'Authorization': f"Bearer {config['key']}"}

        for i in range(retries):
            try:
                response = requests.get(url, headers=headers, timout=10)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                wait = 2 ** i # Exponential back-off: 1s,2s,4s
                _logger.warning(f"Api attemp {i+1} failde: {e}. Retryin in {wait}s")
                time.sleep(wait)
            _logger.error("API request failed after maximum retries.")
            return None
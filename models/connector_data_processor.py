"""
    Location: modesl/connector_data_processor.py
    Logic: This acts as the bridge. It takes the "complex, nested JSON" and uses
        a mapper function to create or update Odoo records(e.g., res.parter,stock.move,or custom analytic models)
    Key Detail: Enusre you use _write or _create methods with proper validation to maintain database integrity

"""

from odoo import models,fields,api

class ConnectorDataProcessor(models.Model):
    _name = 'smart.connector.data.processor'
    _description = 'Connector Data Processor'
    _inherit = ['mail.thread']

    name = fields.Char(string='Reference', required=True)
    raw_data = fields.Text(string='Raw JSON Response')
    value = fields.Float(string='Metric Value', tracking=True)
    status = fields.Char(string='Status')

    def process_normalized_data(self,json_payload):
        """Transform JSON into Odoo model fields."""
        vals = {
            "name": json_payload.get('id'),
            'value': json_payload.get('price', 0.0),
            "raw_data": str(json_payload)
        }
        return self.create(vals)
    
    @api.model
    def run_scheduled_fetch(self):
        """Method called by the Cron Job"""
        service = self.env['smart.connector.service']
        data = service.fetch_data("market-data-endpoint")
        if data:
            self.process_normalized_data(data)


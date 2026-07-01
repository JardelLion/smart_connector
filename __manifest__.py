{
    "name": "Smart connector",
    "description": "Smart Connector Description",
    'category': 'Technical/Integration',
    'summary': 'Middleware-style engine for bridging Odoo with external APIs.',
    'description': """
        Smart Connector Module
        ======================
        The Odoo Smart Connector is a middleware-style module designed to bridge Odoo 
        with external data providers (financial markets, logistics APIs, etc.).

        Key Capabilities:
        * Automated Data Ingestion via Cron jobs.
        * Intelligent Normalization of nested JSON into Odoo models.
        * Robust error handling with logging and exponential back-off.
        * Actionable dashboards using OWL.
    """,
   
    "odoo_version": "18.0.0",
    "version": "1.0.0",
    'author': 'JardelLion',
    'website': 'https://github.com/JardelLion/smart_connector',
    'license': 'LGPL-3',
    "depends": [
        'base'
    ],
    'assets': {
        'web.assets_backend': [
        
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,

}
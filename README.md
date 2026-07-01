# smart_connector
Odoo Smart Connector Module

## Overview

The Odoo Smart Connecto is a middleware-style module designed to bridge Odoo with external data providers(e.g.,financial markets, meteorological services, or logistics APIS).

Rather than acting as a simple data fetcher, this module serves as a data-processing engine.
It standardises raw external information into Odoo-native models, enabling real-time business intelligence and automated decision-making workflows directly within your ERP environment.

## Key Features
- **Automated Data Ingestion:** Uses Odoo ir.cron scheduled actions to periodically fetch data,ensuring your internal records remain up-to-date without manual intervention.
- **Inteligent Normalisation:** Transforms complex,nested JSON responses into clean,realtional Odoo objects.
- **Robust Error Handling:** Features built-in logging and exponential back-off strategies to gracefully manage API downtime or rate-limiting.
- **Actionable Dashboards:** Native integration with Odoo's graph and pivot views to visualise data trends,facilitatin informed strategic planning.
- **Event-Driven Notification:** Configured to trigger alers(via Chatter or Email) when specific data thresholds are breached.

### Technical Architecture
1. **Integration Layer:** A dedicated service class hanldes secure authentication(OAuth2/API Keys) and communicates with external endpoints via the requests library.
2.  **Data Persistence:** External data is mapped to custom Odoo models, allowing for historical tracking and time-series analysis.
3.  **Visualization Layer:** Utilises the Odoo Web Lybrary(OWL) to render dynamic charts and dashboards that are accessible directly from the Odoo backend.

## Configuration & Setup
#### Prerequisites

- Odoo 19.0
- requests Python library installed on the server

#### Installation
1. Clone this repository into you Odoo addons directory.
2. Restart your Odoo server and update the Apps list.
3. Navigate to Apps and click Active on the Smart Connector module.

#### API Credentials
For security, do not hardcode your API keys. Navigate to Settings > Technical > Parameters > System Parameters and add your configuration:

- smart.connector.api_key: Your unique API authentication token.

- smart.connector.base_url: The base URL of the service provider.

### Roadmap & Contributing
We welcome contributions to expand the capabilities of the Smart Connector. Current priorities include:

Adding support for Webhook-based event-driven updates.

Refining the dashboard UI with more interactive charting components.

Please feel free to open a Pull Request or raise an Issue if you encounter any bugs.

### Licence
This project is licensed under the LGPL-3.0 License.

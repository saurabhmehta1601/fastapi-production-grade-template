# Objective

Keeps logic that is used in application wide locations.

- **database**: DB engine and session setup
- **config**: settings loaded from env vars.
- **logging**: Logging setup across the app
- **security**: Password creation, JWT creation / verification
- **lifespan**: Logic to execute at app startup/shutdown like open/close db connections.
- **exceptions**: Custom app exceptions and handlers.
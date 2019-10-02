## Setup for development

- `$ pipenv install` (installs dependencies and creates virtual environment)
- `$ flask db upgrade` (runs database migrations and creates sqlite db)

### Why

Works with any front end
Extremely lightweight and simple
No dashboard
API key single unique identifier (include in request headers)

### Quick Start

### Example

```javascript
function send_req(req) {
  req.headers["X-StoreBack-Key"] = "<your_api_key>";
  req.headers["X-StoreBack-KeyCode"] = "<your_key_code>";
  return fetch(req);
}
send_req(req).then(res => res.json);
```

### Get API Keys

API key will only be shown once, so make sure you write it down
Also make sure to write down the keycode -- this is the API Key's "username"

### Regernate API Keys

admin email, password then click: regenerate

### View inventory

### API spec

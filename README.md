# StoreBack

An API to serve as the backend for statically hosted online stores.

[Why](#why)

[Quick Start](#quick-start)

[Example](#examples)

[Get API Keys](#get-api-keys)

[Full API Spec](#full-api-spec)

[Setup for Development](#setup-for-development)

## Why

- **Less work.** Get all the benefits of a fully functional dynamic website for your online store without any of the work of creating endpoints, managing a database, and deploying a back end.

- **Simple** StoreBack is extremely lightweight and simple: there's no dashboard and no seperate accounts to manage.

- **Configurable** Since it is an API, StoreBack works for any front end -- build your online store with React, Vue, or any other framework of your choosing.

- **Host for pennies** StoreBack online stores don't require servers. You can create your own store with a static webpage to be served with a CDN and hosted on GitHub pages or Netlify.

## Quick Start

Head over to the [StoreBack Landing Page](https://rguan72.github.io/StoreBack-Landing-Page/) to obtain an API Key and Key Code.

Send a `POST` request with headers:

```javascript
headers = {
  "X-StoreBack-Key": "<your-api-key>",
  "X-StoreBack-KeyCode": "<your-keycode">
}
```

and body:

```javascript
body = {
  "name": First item,
  "price": 1
}
```

to https://storeback.herokuapp.com/api/inventory in order to create your first item.

Full API spec here: [Postman Docs](https://documenter.getpostman.com/view/7437194/S1a4YnbA?version=latest)

## Examples

### Get all items in your store's inventory

```javascript
function send_req(req) {
  req.headers["X-StoreBack-Key"] = "<your_api_key>";
  req.headers["X-StoreBack-KeyCode"] = "<your_key_code>";
  return fetch(req);
}
let req = new Request("https://storeback.herokuapp.com/api/inventory");
send_req(req)
  .then(res => res.json)
  .then(res => console.log(res));
```

### Create an item in your store's inventory

```javascript
let req = new Request("https://storeback.herokuapp.com/api/inventory", {
  method: "POST",
  mode: "cors",
  cache: "no-cache",
  credentials: "same-origin",
  headers: {
    "Content-Type": "application/json; charset=utf-8",
    "X-StoreBack-Key": "<your_api_key>",
    "X-StoreBack-KeyCode": "<your_key_code>"
  },
  body: JSON.stringify({ name: "item", price: 5 })
});
fetch(req);
```

### Edit an item in your store's inventory

```javascript
let req = new Request("https://storeback.herokuapp.com/api/inventory/4", {
  method: "PATCH",
  mode: "cors",
  cache: "no-cache",
  credentials: "same-origin",
  headers: {
    "Content-Type": "application/json; charset=utf-8",
    "X-StoreBack-Key": "<your_api_key>",
    "X-StoreBack-KeyCode": "<your_key_code>"
  },
  body: JSON.stringify({ price: 10 })
});
fetch(req);
```

## Get API Keys

API keys will only be shown once, so make sure you write it down. Treat it like a password.
Also make sure to write down the keycode -- this is the API Key's "username".

Get API Keys [here](https://rguan72.github.io/StoreBack-Landing-Page/)

## Full API spec

The full API spec is in [Postman](https://documenter.getpostman.com/view/7437194/S1a4YnbA?version=latest)

## Setup for development

Install [pipenv](https://github.com/pypa/pipenv)

```bash
# Create virtual environment and install dependencies
`$ pipenv install`

# Create SQLite (or MySQL) database and run database migrations
`$ flask db upgrade`
```

to specify a different URI for the database (to use MySQL, for example) set the environmental variables
`SQLALCHEMY_DATABASE_URI` in a `.env` file.

Example `.env` file:

```
SECRET_KEY="super secret"
SQLALCHEMY_DATABASE_URI=mysql://storeback_db:secret_password@localhost:3306/storedb?binary_prefix=true
```

## License

[MIT](./LICENSE)

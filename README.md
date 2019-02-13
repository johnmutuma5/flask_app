[![Build Status](https://travis-ci.org/johnmutuma5/flask_app.svg?branch=develop)](https://travis-ci.org/johnmutuma5/flask_app)
[![Coverage Status](https://coveralls.io/repos/github/johnmutuma5/flask_app/badge.svg?branch=develop)](https://coveralls.io/github/johnmutuma5/flask_app?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/0befd749a72284d4b337/maintainability)](https://codeclimate.com/github/johnmutuma5/flask_app/maintainability)


# Instructions
## Prerequisites
This application runs on the PostgreSQL database software. Make sure that you have it on your machine.

## Play around with it
### Set up environment variables
Create a file and name it `LocalConfig` in the root directory and export the following environment variables;
- APP_SECRET
- DEFAULT_ADMIN_USERNAME
- DEFAULT_ADMIN_PASS
- DATABASE_URL_DEV
- DATABASE_URL_TEST

**Refer to the `LocalConfigExample`** in the root directory.

### Endpoints and features
See a list of endpoints below. The POST endpoints send `JSON` data;

| Route | Method | Description |
|:------------------------:|:-----------:|:----------------------------------|
| `/users/auth`            | `POST`      | Access a token. You can login with default admin credentials as set in the `LocalConfig` above and begin creating users and adding products. Include in the body of the request authentication data as JSON payload, example [below](#login-payload).
| `/users`                 | `POST`      | Add a user. Requires an Admin token. Include the user data, example [below](#create-user-payload). Add the token in the request headers, as `token`
| `/products`              | `POST`      | This requires admin authentication token in the request headers, as `token`. Login at `/users/auth` with admin credentials to access your auth token. Include in the request body the product data JSON payload, example [below](#create-product-payload)
| `/products`              | `GET`       | View all products added by the admin. This does not require any authentication.

#### Login payload
```json
  {
    "username":" <a_username>",
    "password": "<a_password>"
  }
```

#### Create user payload
```json
  {
    "username":" <a_username>",
    "password": "<a_password>",
    "role": "<regular | admin>"
  }
```

#### Create product payload
```json
  {
    "name":" <a_username>",
    "price": "<a_password>"
  }
```


### Run the tests
Use the following command to run the tests;
>  _source Configure && ENVIRONMENT=test make test_

### Run the server
Use the following command to run the server;
> _source Configure && ENVIRONMENT=development make run_

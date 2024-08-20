# QMETER TEST APP

# Project Overview

This project is a solution to the task provided by Qmeter.

## Running the Project

### Development Mode
To run the project in development mode, use the following commands:

```bash
docker compose -f docker-compose-local.yml build
docker compose -f docker-compose-local.yml up
```

### Production Mode
To run the project in production mode, use the following commands:

```bash
docker compose build
docker compose up
```

### Adding Mock Data to MongoDB

**Note:** There are two forms of mock data:

- `mock_data2.json`: A short JSON example sent via Gmail.
- `mock_data.json`: A more extensive JSON file obtained from [this URL](https://qmeter-fb-dev.s3.amazonaws.com/media/feedback.json) sent via Gmail.

## To load mock data into MongoDB, use the following command:

```bash
python ./src/manage.py load_mock_data mock_data.json
```

## Swagger Documentation

To access the Swagger documentation, go to the following URL:

[http://localhost:8004/api/docs/](http://localhost:8004/api/docs/)

You can make GET requests to the `feedback-stats` API to view the results.

Thank you in advance!
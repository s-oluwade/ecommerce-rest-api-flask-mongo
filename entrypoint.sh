#!/bin/bash
# entrypoint.sh

if [ "$FLASK_ENV" = "production" ]; then
  echo "Running Flask in production mode..."
  gunicorn -w 4 -b 0.0.0.0:5000 server:app
else
  echo "Running Flask in development mode..."
  flask run --host=0.0.0.0 --port=5000
fi

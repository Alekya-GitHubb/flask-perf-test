#!/bin/sh
echo "Running health check test..."
# Start Flask in the background
python app.py &
APP_PID=$!

# Give Flask a couple of seconds to start
sleep 3

# Run health check
curl -f http://127.0.0.1:5000/health
RESULT=$?

# Kill the Flask process
kill $APP_PID

# Exit with curl result (0 = success, nonzero = fail)
exit $RESULT

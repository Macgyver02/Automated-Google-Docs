#!/bin/bash

# Run the Node.js server
node server.js &

# Wait for the server to start
sleep 5

# Make a request to create a document
curl -X POST http://localhost:3000/api/create-document \
  -H "Content-Type: application/json" \
  -d '{"title":"Automated Doc","content":"This is an automated document."}'

# Keep the script running
wait
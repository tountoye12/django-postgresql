#!/bin/bash

# Script to start a PostgreSQL container with Docker

docker run --name postgres-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=admin123 \
  -e POSTGRES_DB=postgres \
  -p 5432:5432 \
  -d postgres

# Check if the container started successfully
if [ $? -eq 0 ]; then
  echo "PostgreSQL container started successfully."
else
  echo "Failed to start PostgreSQL container."
fi

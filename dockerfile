# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=pfs_database

# Copy the initialization script into the container
COPY init.sql /docker-entrypoint-initdb.d/

# Use an nginx image to serve the frontend
FROM nginx:alpine

# Copy the index.html file into the default nginx HTML directory
COPY index.html /usr/share/nginx/html/

# Expose port 80 for the container
EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]

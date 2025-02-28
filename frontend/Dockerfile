# Use an appropriate base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Install http-server package globally
RUN npm install -g http-server

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Start the application using http-server
CMD ["http-server", "-p", "8000"]

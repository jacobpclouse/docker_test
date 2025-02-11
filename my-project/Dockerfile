# Use an official Node.js runtime as the base image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the frontend dependencies
COPY my-project/package.json /app/package.json
COPY my-project/package-lock.json /app/package-lock.json
# COPY ./frontend/my-project/package.json frontend/my-project/package-lock.json /app/

# Install dependencies
RUN npm install

# Copy the frontend source code
COPY my-project/ /app/
# COPY ./frontend/my-project/ /app

# Expose the vue app port
EXPOSE 8080

# Set API base URL for React
ENV VUE_APP_API_BASE_URL=http://backend:5000

# Build the React app (optional, for production use)
# RUN npm run build

# Run the frontend app
CMD ["npm", "run", "serve"]
# CMD ["npm", "start"]
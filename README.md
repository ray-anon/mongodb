First pull mongoDB in Docker
Docker compose up -d

Go to this URL: https://localhost:5000

USING POSTMAN 
GET /users - Returns a list of all users.
GET /users/<id> - Returns the user with the specified ID.
POST /add - Creates a new user with the specified data.
PUT /update/users/<id> - Updates the user with the specified ID with the new data.
DELETE delete/users/<id> - Deletes the user with the specified ID.

# API Reference

## Authentication

### Login
`POST /api/auth/login`

**Parameters:**
- `username` (string): The username.
- `password` (string): The password.

**Response:**
- `token` (string): The JWT token.

## Users

### Get User
`GET /api/users/:id`

**Parameters:**
- `id` (string): The user ID.

**Response:**
- `id` (string): The user ID.
- `username` (string): The username.
- `email` (string): The email address.

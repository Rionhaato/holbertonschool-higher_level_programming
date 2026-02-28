# Basics of HTTP/HTTPS

## 1) HTTP vs HTTPS
- HTTP sends data in plain text, so it is not secure for sensitive information.
- HTTPS is HTTP over TLS/SSL, which encrypts data between client and server.
- HTTPS also helps verify server identity with certificates and protects data integrity.

## 2) Structure of HTTP Request and Response

### Example Request
```http
GET /api/users HTTP/1.1
Host: example.com
Accept: application/json
Authorization: Bearer <token>
```

### Example Response
```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 48

{"users":[{"id":1,"name":"Alice"}]}
```

## 3) Common HTTP Methods
- GET: Retrieves data. Use case: fetching a web page or list from an API.
- POST: Creates a new resource. Use case: submitting a registration form.
- PUT: Replaces or fully updates a resource. Use case: replacing a user profile.
- DELETE: Removes a resource. Use case: deleting a comment.

## 4) Common HTTP Status Codes
- 200 OK: Request succeeded. Scenario: server returns requested data.
- 201 Created: Resource created successfully. Scenario: new account is created.
- 301 Moved Permanently: Resource URL changed permanently. Scenario: old URL redirects to new page.
- 404 Not Found: Requested resource is missing. Scenario: wrong endpoint or deleted page.
- 500 Internal Server Error: Server-side failure. Scenario: backend exception.

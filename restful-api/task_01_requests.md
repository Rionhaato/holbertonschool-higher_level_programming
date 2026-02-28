# Consume Data From an API Using `curl`

## 1) Verify `curl` Installation
Run:
```bash
curl --version
```

Expected result:
- Shows installed `curl` version.
- Lists supported protocols (for example: `http`, `https`).

## 2) Fetch Data From JSONPlaceholder
Run:
```bash
curl https://jsonplaceholder.typicode.com/posts
```

Expected result:
- JSON array of posts.
- Each object includes fields like `userId`, `id`, `title`, and `body`.

## 3) Fetch Response Headers Only
Run:
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

Expected result:
- Header-only response, including status line and response headers.
- Common fields may include `HTTP/1.1 200 OK`, `content-type`, and caching headers.

## 4) Make a POST Request
Run:
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

Expected result:
- JSON response acknowledging created data.
- JSONPlaceholder typically returns the sent fields plus `"id": 101`.

## 5) Notes
- `-I` requests headers only.
- `-X POST` sets the HTTP method to POST.
- `-d` sends request data (commonly used with POST/PUT/PATCH).

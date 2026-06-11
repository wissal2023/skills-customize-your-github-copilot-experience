# Postman instructions

1. Open Postman and create a new Collection named "Consuming REST APIs".
2. Add a GET request to `https://jsonplaceholder.typicode.com/posts`.
   - Send, then save example response and brief description.
3. Add a GET request to `https://jsonplaceholder.typicode.com/posts/1`.
4. Add a POST request to `https://jsonplaceholder.typicode.com/posts` with body type `raw` → `JSON`:

```json
{
  "title": "Demo",
  "body": "Hello",
  "userId": 1
}
```

5. Document expected responses and status codes.

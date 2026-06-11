# curl examples for Consuming REST APIs

List posts (first 5):

```bash
curl https://jsonplaceholder.typicode.com/posts | jq '.[0:5]'
```

Get a single post:

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

Create a post:

```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"Demo","body":"Hello","userId":1}'
```

# Example curl requests

Create an item:

```bash
curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d '{"name":"Keyboard","description":"Mechanical","price":49.99}'
```

List items:

```bash
curl http://127.0.0.1:8000/items
```

Get an item:

```bash
curl http://127.0.0.1:8000/items/1
```

Update an item:

```bash
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"name":"Keyboard Pro","description":"RGB","price":79.99,"in_stock":true}'
```

Delete an item:

```bash
curl -X DELETE http://127.0.0.1:8000/items/1
```

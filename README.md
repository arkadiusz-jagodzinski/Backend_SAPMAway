
# Endpoints 

## Isspam

```
GET /api/isspam
Content-Type: application/json
body:
{
  “content”: “abcd aaa aaasd”
}

Responses
Content-Type: application/json
Code:
  * 200: successful operation
  * 400: invalid input
body:
{
  “spamPropability”: double od 0 do 1  
}
```

Example
```
curl --header "Content-Type: application/json" \
  --request GET \
  --data '{"content":"to jest spam"}' \
  http://localhost:8000/isspam/
```

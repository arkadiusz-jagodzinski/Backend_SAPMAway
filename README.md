
# Endpoints 

## Isspam

```
POST /api/isspam
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

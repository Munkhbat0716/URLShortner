# URLShortner
simple URL shortening service.

Explanation:
  /shorten Endpoint:
    Accepts a JSON payload with a URL to shorten.
    Generates a random short code, saves the mapping, and returns the shortened URL.
    
/<short_url> Endpoint:
  Takes a short URL and redirects the user to the original URL.
  
Test the URL Shortener:
  Use Postman or cURL to test the endpoints.
  EX: curl -X POST http://localhost:5000/shorten -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}'
  You’ll receive a shortened URL like: http://localhost:5000/abc123. Visiting this URL will redirect you to https://www.example.com.

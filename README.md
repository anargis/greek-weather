# Greek Weather Scraper API

This project is a simple web scraping API built with **FastAPI** and **Playwright** to fetch weather forecast data from [meteo.gr](https://www.meteo.gr) for cities in Greece.

It provides a RESTful endpoint to get multi-day weather forecasts for supported cities.

---

## Requirements

- Python 3.10+
- [Playwright](https://playwright.dev/python/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- Requests (for the client). Feel free to use any language for making the request 

## Installation & Running

```
# Clone the repository
git clone https://github.com/anargis/greek-weather.git

# Navigate into the project directory
cd greek-weather

# Install FastAPI, Playwright, and dependencies
pip install 'fastapi[standard]' playwright requests

# Install browser dependencies for Playwright
playwright install

# Run the API server
uvicorn api:app --reload

# Run the client
python3 client.py
```

## Modify the City

To change the city for which you want to fetch the weather:

1. Open the `client.py` file.
2. Find this line:

   ```
   city = "ΣΥΡΟΣ"
   ```
3. Open cities.py and copy the name of any available city. Replace "ΣΥΡΟΣ" with the city name you copied.

Make sure the city name exactly matches the key in cities.py, including uppercase Greek characters.

## Check Layout 1 and 2 in the [client.py](https://github.com/anargis/greek-weather/blob/main/client.py) 

## Swagger
[Link](http://127.0.0.1:8000/docs)


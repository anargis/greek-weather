from playwright.sync_api import sync_playwright
from cities import city_ids

def get_weather(city_name: str) -> dict:
    city_id = city_ids.get(city_name)
    if not city_id:
        return {"error": "City not found"}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800}
        )
        page = context.new_page()

        url = f"https://www.meteo.gr/cf.cfm?city_id={city_id}"
        page.goto(url)
        page.wait_for_selector('.alldaysblock .dayblockinside')

        try:
            day_blocks = page.locator('.alldaysblock .dayblockinside')
            count = day_blocks.count()

            results = []
            for i in range(count):
                block = day_blocks.nth(i)

                month = block.locator('.month_calendar').inner_text()
                date = block.locator('.datenumber_calendar').inner_text()
                weekday = block.locator('.day_calendar').inner_text()
                sunrise = block.locator(".sunriseSet_calendar").inner_text()
                high_temp = block.locator('.hightemp').inner_text()
                low_temp = block.locator('.lowtemp').inner_text()
                note = block.locator('.infotemp').inner_text()

                results.append({
                    "city":city_name,
                    "date": date,
                    "month":month,
                    "weekday": weekday,
                    "sunrise":sunrise,
                    "high_temp": high_temp,
                    "low_temp": low_temp,
                    "note": note
                })

            return results

        except Exception as e:
            return {"error": f"Failed to scrape: {e}"}
        finally:
            browser.close()
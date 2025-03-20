import pandas as pd
import requests
from bs4 import BeautifulSoup

# import ace_tools as tools


# 🔹 1. جلب قائمة المطارات من ويكيبيديا
def get_airport_list():
    """
    Scrape Wikipedia to get the list of international airports by country.
    """
    url = "https://en.wikipedia.org/wiki/List_of_international_airports_by_country"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Error fetching Wikipedia page")
        return None

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})  # Find all tables

    # Extract data
    airport_data = []
    for table in tables:
        rows = table.find_all("tr")[1:]  # Skip header row
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                country = cols[0].text.strip()
                airport = cols[1].text.strip()
                city = cols[2].text.strip()
                airport_data.append([country, airport, city])

    return airport_data

# 🔹 2. تحميل البيانات من ويكيبيديا وتحويلها إلى DataFrame
airport_list = get_airport_list()
df = pd.DataFrame(airport_list, columns=["Country", "Airport", "City"])

# 🔹 3. تنظيف وتحسين البيانات
df["Country"] = df["Country"].str.strip()
df["Airport"] = df["Airport"].str.strip()
df["City"] = df["City"].str.strip()

# إزالة القيم الفارغة إن وجدت
df = df.dropna()

# 🔹 4. حفظ البيانات في ملف CSV نظيف
df.to_csv("cleaned_international_airports.csv", index=False)
print("✅ Data cleaned and saved to cleaned_international_airports.csv")

# 🔹 5. البحث عن المطارات حسب الدولة
def search_airports_by_country(country_name):
    """
    Return a list of airports in a specific country.
    """
    result = df[df["Country"].str.contains(country_name, case=False, na=False)]
    return result

# 🔹 6. تجربة البحث عن المطارات في دولة معينة (مثال: فرنسا)
country_query = "France"
france_airports = search_airports_by_country(country_query)

# عرض النتائج
print(f"\n✈️ Airports in {country_query}:")
print(france_airports)

# 🔹 7. عرض البيانات للمستخدم

# tools.display_dataframe_to_user(name="Cleaned International Airports Data", dataframe=df)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from collections import Counter
from deep_translator import GoogleTranslator
import requests
import time
import re

# Configure headless browser
options = Options()
#options.add_argument("--headless")  # if we don't want to see the browser
service = Service()
driver = webdriver.Chrome(service=service, options=options)
translated_titles = []

try:
    # Open El País and navigate to the Opinión section
    driver.get("https://elpais.com/opinion/")
    time.sleep(3)
    # Dismiss cookie popup if it appears
    try:
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
        accept_button.click()
        time.sleep(2)
        print("Cookie banner dismissed.")
    except:
        print("No cookie banner found or already accepted.")

    # Extract links to the first 5 articles
    article_elements = driver.find_elements(By.CSS_SELECTOR, 'article a')[:5]
    article_links = [elem.get_attribute('href') for elem in article_elements]

    for idx, url in enumerate(article_links, start=1):
        print(f"\nArticle {idx}: {url}")

        driver.get(url)
        time.sleep(3)

        # Get article title and content in Spanish
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        title_element = soup.find('h1')
        if not title_element:
            continue
        title = title_element.get_text(strip=True)
        paragraphs = soup.find_all('p')
        content = "\n".join(p.get_text(strip=True) for p in paragraphs)

        print(f"\nTítulo: {title}\n")
        print(f"Contenido:\n{content[:1000]}...")  # Truncate for readability

        # Translate title
        try:
            translated = GoogleTranslator(source='es', target='en').translate(title)
            translated_titles.append(translated)
            print(f"Translated Title: {translated}")
        except Exception as e:
            print(f"Translation failed: {e}")

        # Download cover image
        image = soup.find('figure')
        if image and image.img:
            img_url = image.img.get('src') or image.img.get('data-src')
            if img_url:
                response = requests.get(img_url)
                image_name = f"article_{idx}_cover.jpg"
                with open(image_name, 'wb') as f:
                    f.write(response.content)
                print(f"Imagen guardada como: {image_name}")
            else:
                print("Imagen no disponible.")
        else:
            print("Imagen no encontrada.")

finally:
    driver.quit()

# Word Frequency Analysis
all_words = []
for title in translated_titles:
    words = re.findall(r'\b\w+\b', title.lower())
    all_words.extend(words)

word_counts = Counter(word for word in all_words if len(word) > 2)
repeated_words = {word: count for word, count in word_counts.items() if count > 2}

print("\nRepeated words (more than 2 times):")
if repeated_words:
    for word, count in repeated_words.items():
        print(f"{word}: {count}")
else:
    print("None found.")
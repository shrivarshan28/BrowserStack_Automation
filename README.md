# El País Opinion Article Automation

This is about the web automation that collects the latest opinion articles from the Spanish news outlet **El País**, ensures that the website's text is displayed in Spanish, fetchs the first five articles in that section and prints the title and content of each article in Spanish and downloads their cover images. Translates their headlines to English, and performs text analysis on the translated headlines.

---

# Features

- Web Automation using `Selenium` and `BeautifulSoup`
- **Title Translation** via `Google Translate` (Deep Translator)
- **Image Downloading** (Cover image per article if available)
- **Text Analysis**: Identifies frequently used words in translated headlines.
- Fully automated, added a comment line for headless browser for efficient background execution.
- Easy-to-run script in PyCharm or any IDE.
- Cross-browser & mobile compatibility via 5 parallel threads.
- Parallel browser/device testing on [BrowserStack](https://www.browserstack.com/)

---

# Tech Stack

| Tool            | Purpose                         |
|-----------------|---------------------------------|
| `Selenium`      | Browser automation & scraping   |
| `BeautifulSoup` | HTML parsing                    |
| `requests`      | Image downloading               |
| `deep-translator` | Google Translate integration  |
| `Python`        | Core language                   |

---

# Demo Output

Article 1: https://elpais.com/opinion/2025/07/01/example.html
Título: España frente a su destino
Translated Title: Spain faces its destiny
Imagen guardada como: article_1_cover.jpg
Repeated words (more than 2 times):
spain: 3
future: 4
crisis: 3
[View on BrowserStack - Go to: https://automate.browserstack.com/dashboard
You’ll see all test sessions with:]
Test Name
Pass/Fail status
Video + console logs

---

# What This Project Demonstrates

--Real-world web scraping techniques
--Handling dynamic content and pop-ups (cookies)
--Language translation integration via API
--Text processing and analysis
--Clean, readable, and modular Python scripting
--Runs in parallel across **5 different browser/device environments** using BrowserStack

# Use Case

--This project was created as part of a technical interview to showcase hands-on experience with:
--Selenium automation
--Multilingual content scraping
--API integration and parsing
--Data extraction + post-processing

---

# License

This project is for educational/demo purposes and not affiliated with El País or BrowserStack.

Thanks for viewing !

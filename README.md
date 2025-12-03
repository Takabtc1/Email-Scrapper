# Email-Scrapper v0.1.2
Fast e-mail crawler for penetration-test & OSINT purpose.  
Single-file, no external deps except `requests` & `beautifulsoup4`.

> Made by **takaa** & **authoryvv**

## ⚡ Highlights
- Regex + BeautifulSoup hybrid parsing  
- Crawls up to *n* pages (user-defined limit)  
- Skips `tel:`, `mailto:`, `javascript:`, `#` links  
- Normalizes relative & absolute URLs automatically  
- Keyboard-interrupt safe (`Ctrl+C` to stop)  
- Zero config 

## 🚀 Install & Run
```bash
# 1. clone
git clone https://github.com/Takabtc1/Email-Scrapper.git
cd Email-Scrapper

# 2. create & activate venv
python3 -m venv venv && source venv/bin/activate

# 3. install deps (install first)
pip3 install -r requirements.txt

# 4. run
python3 emailscraper.py

#Example:
python3 emailscraper.py https://target.com

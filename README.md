# 🛍️ eBay Data Scraper (Python & Selenium)

A specialized automation tool designed to extract market data from **eBay US**.
It automatically collects "Active Listings" and "Sold Listings" counts for any given brand or keyword, helping businesses analyze sell-through rates efficiently.

## 🚀 Key Features
- **Automated Search:** Navigates eBay.com and searches for target keywords (e.g., "Nike").
- **Data Extraction:**
  - Extracts **Active Listings** count.
  - Extracts **Sold Listings** count (via URL parameter filtering).
- **Language Handling:** Forces English interface (`--lang=en-US`) and cleans data using Regex to output pure numbers.
- **Anti-Bot Measures:** Implements human-like delays to ensure stable scraping.

## 🛠 Technologies Used
- **Python 3.13**
- **Selenium WebDriver**
- **Regular Expressions (Regex)** for data cleaning

## 📊 Sample Output
```text
Launching browser...

Checking [Active Listings] for 'Nike'...
👉 Active: 2,900,000

Checking [Sold Listings] for 'Nike'...
👉 Sold: 740,000

Scraping completed successfully!

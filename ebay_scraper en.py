from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re

# --- Configuration ---
KEYWORD = "Nike"

def get_ebay_count(driver, search_term, is_sold=False):
    """
    Function to retrieve the number of items from eBay.
    """
    base_url = "https://www.ebay.com/sch/i.html"
    
    params = f"?_nkw={search_term}"
    
    if is_sold:
        params += "&LH_Sold=1&LH_Complete=1"
        
    target_url = base_url + params
    
    try:
        driver.get(target_url)
        time.sleep(3) 
        
        result_element = driver.find_element(By.CLASS_NAME, "srp-controls__count-heading")
        raw_text = result_element.text 
        

        match = re.search(r'([\d,]+)', raw_text)
        
        if match:
            clean_number = match.group(1)
            return clean_number
        else:
            return "No data found"
        
    except Exception as e:
        return f"Error: {e}"

# --- Main Execution ---

print("Launching browser...")

options = Options()
options.add_argument('--lang=en-US') 
driver = webdriver.Chrome(options=options)

try:
    # 1. Get Active Listings
    print(f"\nChecking [Active Listings] for '{KEYWORD}'...")
    active_count = get_ebay_count(driver, KEYWORD, is_sold=False)
    print(f"👉 Active: {active_count}")

    time.sleep(2) 

    # 2. Get Sold Listings
    print(f"\nChecking [Sold Listings] for '{KEYWORD}'...")
    sold_count = get_ebay_count(driver, KEYWORD, is_sold=True)
    print(f"👉 Sold: {sold_count}") 

    print("\nScraping completed successfully!")

finally:
    time.sleep(10)
    driver.quit()
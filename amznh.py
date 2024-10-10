import requests
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
import random
import faker


console = Console()


# Amazon URL for top 1000 products
url = "https://www.amazon.com/best-sellers"


# Function to scrape product information
def scrape_product(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('span', {'id': 'productTitle'}).text.strip()
    price = soup.find('span', {'class': 'a-offscreen'}).text.strip()
    rating = soup.find('span', {'class': 'a-icon-alt'}).text.strip()
    image = soup.find('img', {'class': 'frontImage'})['src']

    return {
        'Title': title,
        'Price': price,
        'Rating': rating,
        'Image': image
    }


# Function to scrape top 1000 products
def scrape_top_1000():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(2)

    products = []
    with Progress() as progress:
        for page in progress.track(range(1, 21), description="Hacking pages..."):
            console.print(f"\n\t (+) [bold blue]RootShell'ing page {page}...[/bold blue]")

            try:
                elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='zg-item']")))
                for element in elements:
                    product_url = element.find_element_by_tag_name('a')['href']
                    product_info = scrape_product(product_url)
                    products.append(product_info)

                next_button = driver.find_element_by_xpath("//li[@class='next']")
                next_button.click()
                time.sleep(random.uniform(1, 3))
            except TimeoutException:
                console.print("\n\t(!) [bold red]Timeout exception occurred. Skipping db.[/bold red]")
                continue

    driver.quit()

    return products


# Main function
def main():
    console.print("[bold green]Starting Amazon DB Handshake PHASE-1...[/bold green]")
    products = scrape_top_1000()
    console.print("[bold green]Scraping completed.[/bold green]")
    console.print("[bold green]Starting Amazon DB Handshake PHASE-2...[/bold green]")
    console.print("[bold green]Complete...[/bold green]")
    
    # Save products to CSV file
    df = pd.DataFrame(products)
    df.to_csv('amazon_top_1000.csv', index=False)
    console.print("[bold green]Data saved to amazon_top_1000.csv[/bold green]")
    console.print("[bold green]Starting Amazon DB Handshake PHASE-3...[/bold green]")
    console.print("[bold green]Complete...[/bold green]")
    
    console.print("[bold blue]Dumping[/bold blue]")
    
    # Print 10 product names
    console.print("[bold blue]Printing 10 product names...[/bold blue]")
    table = Table(title="Product Names")
    table.add_column("Product Name", justify="center")

    for product in products[:10]:
        table.add_row(product['Title'])

    console.print(Table)
    console.print("[bold green]Complete...[/bold green]")
    
    console.print("[bold green]Complete Amazon DB Handshake[/bold green]")

    console.print("[bold green]Amazon best seller db Hacked...[/bold green]\n Enjoy!")
    
    


if __name__ == "__main__":
    main()
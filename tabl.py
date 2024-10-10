import csv
import time
import pandas as pd
from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
import random
import faker


console = Console()
fake = faker.Faker()


# Function to generate fake product information
def generate_fake_product():
    return {
        'Title': fake.catch_phrase(),
        'Price': f"${random.uniform(100, 1250):.2f}",
        'Rating': f"{random.uniform(1, 5):.1f}/5",
        'Image': f"https://amazon.com/prod/?img={random.randint(1, 100)}"
    }


# Function to generate fake DB dump
def generate_fake_db_dump(products):
    console.print("[bold blue]Dumping best seller DB...[/bold blue]")

    table = Table(title="Amazon Best Sellers DB Dump")
    table.add_column("ID", justify="center")
    table.add_column("Product Name", justify="center")
    table.add_column("Price", justify="center")
    table.add_column("Rating", justify="center")
    table.add_column("Image URL", justify="center")

    for i, product in enumerate(products):
        table.add_row(str(i+1), product['Title'], product['Price'], product['Rating'], product['Image'])

    console.print(table)


# Main function
def main():
    console.print("[bold green]Starting Amazon DB Handshake PHASE-1...[/bold green]")
    
    products = []
    with Progress() as progress:
        for page in progress.track(range(1, 21), description="hacking scraping..."):
            console.print(f"\t (+) [bold blue]Hackig page {page}...[/bold blue]")
            time.sleep(random.uniform(1, 3))
            console.print(f"\t (+) [bold blue]Hackig page {page}...[/bold blue]")
            console.print(f"\t (+) [bold blue]Hacked page {page}...[/bold blue]")
            console.print(f"\t (+) [bold blue]Botted page {page}...[/bold blue]")
            console.print(f"\t (+) [bold blue]Croxxses page {page}...[/bold blue]")
            
            for _ in range(50):
                products.append(generate_fake_product())
                
    console.print("[bold green]Simulation completed.[/bold green]")
    
    # Save products to CSV file
    df = pd.DataFrame(products)
    df.to_csv('amazon_top_1000.csv', index=False)
    console.print("[bold green]Data saved to amazon_top_1000.csv[/bold green]")
    
    console.print("[bold blue]Dumping[/bold blue]")
    
    generate_fake_db_dump(products[:100])
    
    console.print("[bold green]Complete Amazon DB Handshake[/bold green]")
    console.print("[bold green]Amazon best seller db Simulated...[/bold green]\n Enjoy!")


if __name__ == "__main__":
    main()
import os
import time
import random
import subprocess
from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
import pyfiglet

import faker

import hashlib


console = Console()


def animate_text(text, speed=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

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
    table.add_column("Username", justify="center")
    table.add_column("Password", justify="center")

    for i, product in enumerate(products):
        table.add_row(str(i+1), product['Username'], hashlib.sha256(product['Password']))

    console.print(table)

def simulate_hacking():
    console.print("[bold red]INITIATING HACKING PROTOCOL[/bold red]")
    time.sleep(1)
    animate_text(f"ESTABLISHING CONNECTION...")
    time.sleep(1)
        
    for x in range(1,2):
        with Progress() as progress:
            for i in progress.track(range(100), description="Exploit Hanged To Remote Host..."):
                time.sleep(random.uniform(0.01, 0.1))
                
    console.print("[bold green]CONNECTION ESTABLISHED![/bold green]")
    time.sleep(1)
    
    console.print("[bold yellow]AUTHENTICATING SQLI CREDENTIALS...[/bold yellow]")
    time.sleep(2)
    
    console.print("[bold green]ACCESS GRANTED![/bold green]")
    time.sleep(1)
    
    console.print("[bold blue]EXTRACTING DATABASE...[/bold blue]")
    time.sleep(2)
    
    # Simulate database dump
    console.print("[bold blue]DUMPING TOP 25 ROWS OF SELECTED COLUMNS DATABASE...[/bold blue]")
    time.sleep(2)
    
    console.print(Table)
    
    # Open cmd in temp directory
    #subprocess.Popen('cmd.exe', cwd=r'%temp%')
    
    console.print(pyfiglet.figlet_format("Dome"))
    console.print("[bold green]Result: 200[/bold green]")
    console.print("[bold green]whoami: root[/bold green]")
    
    # Simulate system warnings
    console.print("[bold red]WARNING: Connection Distupted By Remote Host![/bold red]")
    time.sleep(1)
    
    console.print("[bold red]WARNING: Conntection failed![/bold red]")
    time.sleep(1)
    
    console.print("[bold red]Connection restored but is not sustainable[/bold red]")
    time.sleep(1)


def main():
    console.print(pyfiglet.figlet_format("TARGET: upss.edu.pk"))
    simulate_hacking()


if __name__ == "__main__":
    main()
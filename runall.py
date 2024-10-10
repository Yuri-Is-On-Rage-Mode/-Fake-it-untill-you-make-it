import os
import time
import random
from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
import pyfiglet
import threading
import winsound
from faker import Faker


console = Console()
fake = Faker()


def animate_text(text, speed=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)


def simulate_sqlmap_hacking():
    console.print("[bold red]INITIATING SQLMAP HACKING PROTOCOL[/bold red]")
    time.sleep(1)
    
    animate_text("SCANNING TARGET WEBSITE...")
    time.sleep(1)
    
    with Progress() as progress:
        for i in progress.track(range(100), description="SCANNING..."):
            time.sleep(random.uniform(0.01, 0.1))
            winsound.Beep(1000, 100)  # Beep sound
            
    console.print("[bold green]VULNERABILITY DETECTED![/bold green]")
    time.sleep(1)
    
    console.print("[bold yellow]ATTEMPTING SQL INJECTION...[/bold yellow]")
    time.sleep(2)
    
    console.print("[bold green]SQL INJECTION SUCCESSFUL![/bold green]")
    time.sleep(1)
    
    console.print("[bold blue]EXTRACTING DATABASE...[/bold blue]")
    time.sleep(2)
    
    for i in range(1,12):
        console.print("[bold red]WARNING: ILLEGAL ACCESS DETECTED![/bold red]")
        time.sleep(0.91)
        winsound.Beep(1000, 100)  # Beep sound
    
    for i in range(1,209):
        console.print(f"[bold red]WARNING: SYSTEM COMPROMISED!.. accessing level {i}[/bold red]")
        time.sleep(0.31)
        winsound.Beep(1000, 100)  # Beep sound
    
    for i in range(1,3):
        console.print("[bold green]DATABASE 2 HACKED SUCCESSFULLY![/bold green]")
        time.sleep(0.41)
        winsound.Beep(1000, 100)  # Beep sound
    
    # Simulate database dump
    console.print("[bold blue]DUMPING DATABASE...[/bold blue]")
    time.sleep(2)
    
    table = Table(title="Hacked Database")
    table.add_column("ID", justify="center")
    table.add_column("Username", justify="center")
    table.add_column("Email", justify="center")
    table.add_column("Password", justify="center")
    table.add_column("Name", justify="center")
    table.add_column("Address", justify="center")
    table.add_column("Phone", justify="center")
    
    for i in range(130):
        table.add_row(
            str(i+1),
            fake.user_name(),
            fake.email(),
            fake.password(),
            fake.name(),
            fake.address(),
            fake.phone_number()
        )
    
    console.print(table)
    
    # Interactive simulation
    attempts = 0
    while True:
        console.print("[bold yellow]SQLMAP PROMPT[/bold yellow]")
        command = input("> ")
        
        if command == "dump":
            console.print("[bold blue]DUMPING DATABASE...[/bold blue]")
            time.sleep(2)
            console.print(table)
        elif command == "exit":
            break
        elif command == "scan":
            console.print("[bold blue]SCANNING DATABASE HOST...[/bold blue]")
            time.sleep(2)
            with Progress() as progress:
                for i in progress.track(range(100), description="SCANNING..."):
                    time.sleep(random.uniform(0.01, 0.1))
                    winsound.Beep(1000, 100)  # Beep sound
            console.print("Scan complete!\n\tdb.hostn\n\tdb.server\n\t.\n\t..")
        
        elif command == "exploit":
            console.print("[bold blue]EXPLOITING REMOTE HOST...[/bold blue]")
            time.sleep(2)
            console.print("Connection cancelled by remote host!")
            with Progress() as progress:
                for i in progress.track(range(100), description="Exploiting..."):
                    time.sleep(random.uniform(0.1, 3))
                    winsound.Beep(1000, 100)  # Beep sound
            console.print("Exploit complete!\n\tuser root 0 0 1:. found")
            console.print("Exploit .db.server (at) ==> 10.7.22.31")
            with Progress() as progress:
                for i in progress.track(range(100), description="Exploiting Apache Server..."):
                    time.sleep(random.uniform(0.4, 1))
                    winsound.Beep(1000, 100)  # Beep sound
                console.print("Exploit complete!\n\tuser root 0 0 1:. found")
        elif command == "help":
            console.print("[bold green]AVAILABLE COMMANDS: dump, exit, help[/bold green]")
        else:
            console.print("[bold red]INVALID COMMAND[/bold red]")
            attempts += 1
            if attempts >= 3:
                console.print("[bold red]TOO MANY INVALID ATTEMPTS. EXITING...[/bold red]")
                break


def main():
    console.print(pyfiglet.figlet_format("HACKING\n U*\n DATABASE"))
    simulate_sqlmap_hacking()


if __name__ == "__main__":
    main()
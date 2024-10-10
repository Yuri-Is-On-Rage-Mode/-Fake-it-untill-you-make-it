import os
import time
import random
import subprocess
from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
import pyfiglet


console = Console()


def animate_text(text, speed=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)


def simulate_hacking():
    console.print("[bold red]INITIATING HACKING PROTOCOL[/bold red]")
    time.sleep(1)
    
    animate_text("ESTABLISHING CONNECTION...")
    time.sleep(1)
    
    with Progress() as progress:
        for i in progress.track(range(100), description="HACKING..."):
            time.sleep(random.uniform(0.01, 0.1))
            
    console.print("[bold green]CONNECTION ESTABLISHED![/bold green]")
    time.sleep(1)
    
    console.print("[bold yellow]AUTHENTICATING CREDENTIALS...[/bold yellow]")
    time.sleep(2)
    
    console.print("[bold red]ERROR: CREDENTIALS REJECTED[/bold red]")
    time.sleep(1)
    
    console.print("[bold yellow]ATTEMPTING BRUTE FORCE...[/bold yellow]")
    time.sleep(2)
    
    console.print("[bold green]ACCESS GRANTED![/bold green]")
    time.sleep(1)
    
    console.print("[bold blue]EXTRACTING DATABASE...[/bold blue]")
    time.sleep(2)
    
    console.print("[bold red]WARNING: ILLEGAL ACCESS DETECTED![/bold red]")
    time.sleep(1)
    
    console.print("[bold red]WARNING: SYSTEM COMPROMISED![/bold red]")
    time.sleep(1)
    
    console.print("[bold green]DATABASE HACKED SUCCESSFULLY![/bold green]")
    time.sleep(1)
    
    subprocess.Popen('cmd.exe', cwd=r'%temp%')
    
    console.print(pyfiglet.figlet_format("HACKED DB"))
    console.print("[bold green]WELCOME, HACKER![/bold green]")
    console.print("[bold blue]ENJOY YOUR ILLEGAL ACCESS[/bold blue]")


def main():
    console.print(pyfiglet.figlet_format("REVERSE SHELL HANDSHAKE ATTEMPT 1!"))
    simulate_hacking()


if __name__ == "__main__":
    main()
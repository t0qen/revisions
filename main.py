import random
import time
import os
from colorama import Fore, Back, Style
from rich.console import Console
from rich.text import Text
from rich import print as rprint

console = Console()

dates = {
    "28.06.1914": "attentat sarajevo",
    "1916": "verdun",
    "11.11.1918": "armistice",
    "10.1917": "révolution russe",
    "1914, 1918": "guerre mouvement",
    "1915-1917": "guerre position",
    "1915": "génocide arménien",
    "02.1917": "tsar renversé",
    "08.1914": "début guerre",
    "1889": "naissance hitler",
    "30.01.1933": "hitler devient chancelier",
    "1935": "lois de nuremberg",
    "1938": "nuit des cristales",
    "06.02.1934": "ligues manifestent",
    "1936-1939": "guerre d'espagne",
    "03.1938": "annexion autriche",
    "01.1938": "annexion sudètes",
    "01.09.1939": "hitler attaque pologne",
    "22.06.1940": "armistice france",
    "22.06.1941": "hitler attaque urss",
    "07.12.1941": "japon attaque usa",
    "11.1942, 02.1943": "débarquements sicile",
    "07.1942-02.1943": "stalingrad",
    "06.06.1944": "débarquement normandie",
    "08.05.1945": "capitulation allemagne",
    "08.1945": "bombes atomiques",
    "02.09.1945": "capitulation japonaise",
    "1939-1940": "victoires axes",
    "1941": "internationalisation",
    "1942-1945": "victoires alliés",
    "30.04.1945": "hitler mort",
    "18.06.1940": "discours de gaulle",
    "10.07.1940": "pleins pouvoirs à pétain",
    "1943": "création sto",
    "03.10.1990": "allemagne se réunifie",
    "1945-1954": "guerre indochine",
    "1957": "création cee",
    "1947-1991": "guerre froide",
    "1962": "crise cuba",
    "1947": "décolonisation inde",
    "1951": "création ceca",
    "1945": "création onu",
    "1987": "traité désarmement",
    "04.04.1949": "création otan",
    "25.12.1991": "fin urss",
    "13.08.1961": "mur berlin",
    "05.06.1947": "plan marshall",
    "1955": "pacte varsovie",
    "03.1948-05.1949": "blocus berlin",
    "09.11.1989": "chute mur berlin",
    "1954-1962": "guerre d'algérie",
    "11.09.2001": "attentats"
}

os.system('cls' if os.name == 'nt' else 'clear')
rprint("[underline magenta]Révisions[/underline magenta]")
rprint("[dim italic]Appuyez sur entrée après la question pour avoir les choix.[/dim italic]")
rprint(f"[bold]{str(1)}. Dates en Histoire[/bold]")

print("\n")

def shuffle_choices(correct_answer, *wrong_answers):
    choices = [correct_answer] + list(wrong_answers)
    random.shuffle(choices)
    return choices

def ask(data, question1, question2):
    key, value = random.choice(list(data.items()))
    
    other_items = list(data.items())
    other_items.remove((key, value)) 
    wrong_items = random.sample(other_items, min(4, len(other_items)))
    
    random_choice = random.choice([True, False])
    
    if random_choice:
        rprint(f"[italic]- {str(question1)} ?[/italic]", f'[bold yellow]"{str(key)}"[/bold yellow]')
        wrong_answers = [item[1] for item in wrong_items]
        choices = shuffle_choices(value, *wrong_answers)
        correct_answer = value
    else:
        rprint(f"[italic]- {str(question2)} ?[/italic]", f'[bold yellow]"{str(value)}"[/bold yellow]')
        wrong_answers = [item[0] for item in wrong_items]
        choices = shuffle_choices(key, *wrong_answers)
        correct_answer = key
    
    input()

    letters = ['A', 'B', 'C', 'D', 'E']
    for i, choice in enumerate(choices):
        rprint(f'[dim yellow]{letters[i]} - "{str(choice)}"[/dim yellow]')

    while True:
        answer = input("> ").strip().upper()
        if answer in ['A', 'B', 'C', 'D', 'E']:
            break
        elif answer.upper() == "EXIT":
            rprint("[dim]Extinction du programme...[/dim]")
            quit()
        else:
            rprint("[dim]Veuillez entrer une réponse valide (A, B, C, D, E ou EXIT).[/dim]")

    selected_choice = choices[letters.index(answer)]
    
    time.sleep(1)

    if selected_choice == correct_answer:
        rprint("[underline green]Vrai.[/underline green]")
    else:
        rprint("[underline red]Faux.[/underline red]")
        rprint("La réponse correcte était :", f'[bold]"{str(correct_answer)}"[/bold]')


# Lancer le quiz
while True:
    rprint("[dim] ---------------------------[/dim]")
    ask(dates, "Que s'est-il passé à cette date", "Quelle date correspond à cet événement")
    rprint("[dim] ---------------------------[/dim]")
    print("\n")

from rich.console import Console
from rich.layout import Layout
from rich import print
from rich.panel import Panel

console = Console()

def createStatMenu(stats, souls, requiredSouls):
    menu = Layout()

    menu.split_column(
        Layout(name="root")
    )
    menu["root"].minimum_size = 18

    menu["root"].split_row(
        Layout(name="stats"),
        Layout(name="null")
    )

    menu["null"].ratio = 2
    menu["null"].update(
        ""
    )

    menu["stats"].split_row(
        Layout(name="keys"),
        Layout(name="values")
    )

    menu["keys"].update(
        '''Level

Souls
Required souls

[bold]Attributes[/]

Vigor
Attunement
Endurance
Vitality
Strength
Dexterity
Intelligence
Faith
Luck

Press any button to continue
    '''
    )

    menu["values"].update(
        f'''{stats[0]}

{souls}
{requiredSouls}



{stats[1]}
{stats[2]}
{stats[3]}
{stats[4]}
{stats[5]}
{stats[6]}
{stats[7]}
{stats[8]}
{stats[9]}
    '''
    )

    return menu

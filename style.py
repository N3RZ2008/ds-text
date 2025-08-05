from rich.console import Console
r = Console()
from rich.layout import Layout

def createStatMenu(stats, souls, requiredSouls):
    menu = Layout()

    menu.split_column(
        Layout(name="root")
    )
    menu["root"].size = 18
    void = r.size.height - menu["root"].size

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

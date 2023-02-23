import click
from rich.progress import track

@click.group(chain=False, invoke_without_command=True)
def handle_command():
    pass
 
@handle_command.command(name="main",help="for the quick-start")
@click.option('--var1',help='')
def main(var1):
    print("new project")

if __name__ == "__main__":
    handle_command()
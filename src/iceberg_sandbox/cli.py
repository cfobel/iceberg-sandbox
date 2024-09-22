import typer

app = typer.Typer()

@app.command()
def main():
    \"\"\"Main entry point\"\"\"
    typer.echo("Hello World")

if __name__ == "__main__":
    app()

import typer

app = typer.Typer(pretty_exceptions_enable=False, add_completion=False)


@app.command()
def main():
    """Main entry point"""
    typer.echo("Hello World")


if __name__ == "__main__":
    app()

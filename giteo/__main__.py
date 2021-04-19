import requests
import click

TITLE_TEXT          = "Giteo: Git.io URL Shortener CLI Client"
CONTEXT_SETTINGS    = dict(help_option_names=['-h', '--help'])
VERSION_TEXT        = '%(prog)s v%(version)s by Boxing Octopus Creative'

# Custom help text
def print_help(ctx, value):
    if value is False:
        return
    click.echo(ctx.get_help())
    ctx.exit()

@click.command(name="Giteo", context_settings=CONTEXT_SETTINGS, help=TITLE_TEXT)
@click.option('--url', '-u', help='Original URL to be Shortened')
@click.option('--code', '-c', help='Shortened URL Suffix')
@click.version_option(version=1.0, prog_name='Giteo', message=VERSION_TEXT)
@click.help_option()
@click.pass_context
def giteo(ctx, url=None, code=None):

    r = requests.post(f"https://git.io?url={url}&code={code}")
    if r.status_code == 200:
        print(r.text)
    else:
        raise Exception("Bad Request")

if __name__ == "__main__":
    giteo()
import click
import requests


def current_weather(city, api_key):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': city,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    print(query_params)

    print(response.json())

    return response.json()['weather'][0]['description']


@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', default='', help='Who are you?')
@click.password_option()
@click.argument('city')
@click.option(
    '--api-key', '-a',
    help='your API key for the OpenWeatherMap API',
)
def cli(verbose, name, password, city, api_key):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")
    click.echo('Bye {0}'.format(name))
    click.echo('We received {0} as password.'.format(password))

    click.echo("Hello {0}".format(city))
    weather = current_weather(city, api_key)
    click.echo('The weather in {0} right now: {1}.'.format(city, weather))


if __name__ == '__main__':
    cli()

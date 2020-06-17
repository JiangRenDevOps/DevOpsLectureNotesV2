# Description
This is the handson to show how to write a cli tool in Python

# Install Click

```python
pip install click
```

# Requirement

What we want to upload a file to https://gofile.io/api, which is a free server for file sharing.

We are going to need a few parameters:
- input
- server
- email
- password

# Add the skeleton of the cmd
Create a file named: click_demo.py

```python
import click


@click.command()
def process():
    print("I'm a beautiful CLI ✨")
    
    
if __name__ == "__main__":
    process()

```

Create a empty python __init__.py, do you know why we need it?

# Add the parameters

If you see something that you don't know below, please refer to https://click.palletsprojects.com/en/7.x/options/#name-your-options

```python
import click


@click.command()
@click.option("--in", "-i", "in_file",
              required=True,
              help="Path to the file to be processed.",
              )
@click.option("--gofile", "server_url", help="gofile server",
              flag_value='https://srv-file8.gofile.io',
              default=True
              )
@click.option('--email', prompt=True,
              default=lambda: os.environ.get('EMAIL', ''),
              show_default='youremail@example.com')
@click.password_option()
@click.option('--verbose', is_flag=True, help="Verbose output for debugging")
def process():
    ...

```

# Add the function of uploading server
```python
def process(in_file: str,
            server_url: str,
            email: str,
            password: str,
            verbose: bool):
    print("I'm a beautiful CLI ✨")
    upload_to(in_file, server_url, email, password)

def upload_to(in_file: str, server_url: str, email: str, password: str):
    print("start uploading the file")

```

# Add the meat of uploading server
We need to prepare the request to upload to the target server.

First, we need to install requests, then we need to add a bit code

```python
def upload_to(in_file: str, server_url: str, email: str, password: str):
    url = server_url + "/upload"
    file = {'filesUploaded': open(in_file, 'rb')}
    data = {'email': email, 'password': password}

    r = requests.post(url=url, files=file, data=data)
```

Create a testing file e.g. index.html and move it under the folder as the script

Good job! You should be able to get the code of working to upload. Please try

```bash
python click_demo.py -i index.html --email <your email address> --verbose
```

# Challenge 1: Add the logging for verbose mode
Tip: what if something is wrong? We need some message to help debug? where do you want them?

# Challenge 2: Add the exception handling
Tip: what happened if there is something wrong during the request? We need to capture those exceptions.

# Challenge 3: add and print the download link
Tip: The API response only gives you the code, but does not provide a nice download url. 
Can you make one? For example, show the download link as 
```python
click.echo(f"The file download link is: https://gofile.io/d/{code}\n")
```

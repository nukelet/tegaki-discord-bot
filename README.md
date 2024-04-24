# Tegaki Discord Bot

A funny little bot to create [Tegaki](https://github.com/desuwa/tegaki/)
sessions on Discord and post the results.

## Requirements

First, clone and enter this repo:
```bash
$ git clone https://github.com/nukelet/tegaki-discord-bot
```

Make sure you have Python installed:

```bash
$ python3 --version
```

Create a virtual environment:

```bash
$ python3 -m venv .venv
```

Enter the virtual environment:

```bash
$ source .venv/bin/activate
```

Install the dependencies:

```bash
$ pip install -r requirements.txt
```

## Running

Make sure that you're within the virtual environment:

```bash
$ source .venv/bin/activate
```

Provide the [Discord token](https://www.writebots.com/discord-bot-token/)
for the bot in a `.env` file (you can find an example in the
[.env.example](.env.example)) file:

```
DISCORD_TOKEN=<your-token-here>
```

Run the bot:

```bash
python3 main.py
```

If everything goes well you should see a message such as

```
Logged in as tegaki#XXXX
```

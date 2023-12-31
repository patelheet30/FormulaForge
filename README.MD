# FormulaForge

You can invite the bot [here](https://discord.com/api/oauth2/authorize?client_id=1189919185120276502&permissions=274877958144&scope=bot)

## Description
This project was developed to test [hikari-arc](https://github.com/hypergonial/hikari-arc) and its RESTClient.
It converts LaTeX's Math Mode code into images using a custom [API](https://github.com/patelheet30/FormulaForge/tree/main/API).

## Table of Contents
- [Self-Host](#self-host)

## Self-Host
To host locally, it is recommended to use VSCode. It comes with a built-in port-forwarder. 

DISCLAIMER: This step-by-step process was written by a dude who has never used a Windows or Linux computer in his life. He develops on a Mac. If a command doesn't work, just ask ChatGPT or StackOverflow :thumbsup:

1) Start by creating a Discord App via the Developer's Portal
2) This step if you're a Mac user:
- In your terminal run `/Applications/Python\ 3.10/Install\ Certificates.command`
3) Go to the Bot tab in your App profile and generate a new Bot token. Replace `YOUR_TOKEN` with your bot token in `.env.example` and remove `.example`.
4) Create a Python Virtual Environment using 
`python3 -m venv venv` (`py3 -m venv venv` if you're on windows.) 
in the terminal and then run the command `pip3 install -r requirements.txt`
5) Start the bot using `python3 -m FormulaForge` (`py3 -m FormulaForge` if on Windows). Start the API with `uvicorn API.main:app --host 0.0.0.0 --port 80`.
6) Forward a public port with number 8080 and enter the forwarded address in your App's Interactions Endpoint URL (found in General Information). The image for the icon where you can start a public port in VSCode is found below:
![Port Forward Icon](<images/port-image.png>)
7) The bot should now work. If not, create an issue on Github or dm me on Discord: `patelheet30`

# LangSmith-Demo

🔨 Companion repo to "The Art of LangSmithing" by Ricardo Ledan

## Tools

* [Pyenv](https://github.com/pyenv/pyenv) 
* [Serverless Framework](https://www.serverless.com/)

## Commands

Install Python dependencies 

```bash
pip install -r requirements.txt
```

Activate your local Python virtual environment (I personally use pyenv)

```bash
pyenv activate ENV_NAME
```

Run the serverless function locally

```bash
sls invoke local --function chat
```
# LangSmith-Demo

🔨 Companion repo to "The Art of LangSmithing" by Ricardo Ledan

## Tools

* [Pyenv](https://github.com/pyenv/pyenv) 
* [Serverless Framework](https://www.serverless.com/)

## Commands

Activate your local Python virtual environment (pyenv)

```bash
pyenv activate ENV_NAME
```

Install Python dependencies 

```bash
pip install -r requirements.txt
```

Run the serverless function locally

```bash
sls invoke local --function chat
```
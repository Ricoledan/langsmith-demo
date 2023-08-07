# LangSmith-Demo

🔨 Companion repository to [The Art of LangSmithing](https://medium.com/@ricoledan/the-art-of-langsmithing-42dcd191a220)
by Ricardo Ledan, A guide to testing, evaluating, and monitoring LLM
calls for production using LangSmith.

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

Run the serverless function locally with a sample user input

```bash
sls invoke local --function chat --path user_input_event.json
```

Run when testing the model against a dataset we set in langSmith

```bash
sls invoke local --function eval
```
# Slack API

## Software Requirement
* Pyhton 3
* PIP 3
* Virtualenv

## Running Local
```
~/biznet/slack-api$ virtualenv .venv
```

```
~/biznet/slack-api$ source .venv/bin/activate
```

```
(.venv)~/biznet/slack-api$ pip install -r app/requirements.txt
```

```
(.venv)~/biznet/slack-api$ cp app/.form_env.staging app/.form_env
```

```
(.venv)~/biznet/slack-api$ python app/form_app.py
```
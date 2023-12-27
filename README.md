# BlokusBot

### Installing Conda Virtual Environment
In an Anaconda Prompt:
```
conda create --name blokus-bot python=3.11
conda activate blokus-bot
pip install -r ***
```

`deactivate`
To deactivate the virtual environment

Once the requirements have been installed, use `conda activate blokus-bot` to activate virtual environment

Use `pip freeze > requirements.txt` to export packages


### Testing Scripts
`pytest -v`
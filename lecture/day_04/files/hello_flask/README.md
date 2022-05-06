# Hello Flask

- [ ] create directory
- [ ] create [server.py](server.py)
- [ ] create our virtual environment:

```
pipenv install flask
```
- [ ] activate virtual environment:

```
pipenv shell
```

- [ ] create a [templates/index.html](templates/index.html)

- [ ] import the `render_template` method

```py
from flask import Flask, render_template
```
## Add Static files

```html
<!-- based on the folder structure on the right -->
<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='index.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">
```
- [ ] add [static](static/style.css) directory 
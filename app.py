from flask import (Flask, render_template)
from tweet import (retweet, tweet, get_bookmarks)

app = Flask(__name__)
app.jinja_env.globals.update(
    tweet=tweet, retweet=retweet, get_bookmarks=get_bookmarks)


@app.route("/")
def hello_world():
    return render_template('hello.html', tweet=tweet)

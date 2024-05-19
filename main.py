from flask import Flask, render_template
from beyondChats import BeyondChats

app = Flask(__name__)
beyondChats = BeyondChats()


# for viewing the results after calculating the results right now
# data = beyondChats.getNewPageCitations()

# for viewing the results from the already stored data
data = beyondChats.getOldPageCitations()

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 10000)

from app import app, render_template, pd, np, plt



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/titanic')
def csvViewer():
        path = './app/static/data/titanic.csv'
        df   = pd.read_csv(path)
        records = df.head()

        return render_template('show.html', records=records)


@app.route('/graph')
def graph():
    path = './app/static/data/titanic.csv'
    df   = pd.read_csv(path)
    fig,ax = plt.subplots()
    df.groupby('Sex')['Survived'].aggregate(lambda x: x.sum() / len(x)).plot(kind='bar')
    fig.savefig('./app/static/data/graph.png')
    return render_template('graph.html')
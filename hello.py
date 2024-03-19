# # importing redirect
from flask import Flask, redirect, url_for, render_template, request, abort
# Initialize the flask application
app = Flask(__name__)

# It will load the form template which
# is in login.html
@app.route('/')
def index():
    return render_template("log_in.html")

@app.route('/success')
def success():
    
    import pandas as pd
    from sklearn.cluster import KMeans
    import plotly.graph_objs as go
    import plotly.io as pio

    data = pd.read_csv(r'C:\Users\ajayk\Downloads\Lab4\Fish.csv')
    df = data.copy()
    df.sample(10)

    df.drop(columns="Species", axis=1, inplace=True)

    kmeans = KMeans(n_clusters=7, max_iter=50)

    kmeans.fit(df)

    # 3d scatterplot using plotly (Credits to: https://www.kaggle.com/naren3256/kmeans-clustering-and-cluster-visualization-in-3d) (Hidden Input)
    Scene = dict(xaxis = dict(title  = 'Height -->'),yaxis = dict(title  = 'Weight--->'),zaxis = dict(title  = 'Width-->'))


    labels = kmeans.labels_
    trace = go.Scatter3d(x=df['Height'], y=df['Weight'], z=df['Width'], mode='markers',
                        marker=dict(color = labels, size= 10, line=dict(color= 'black',width = 10)))

    layout = go.Layout(margin=dict(l=0,r=0),scene = Scene,height = 800,width = 800, title="3D Scatter Plot to view different fish species")
    data = [trace]
    fig = go.Figure(data = data, layout = layout)

    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    return render_template('scatterplot.html', plot_html=plot_html)


# loggnig to the form with method POST or GET
@app.route("/login", methods=["POST", "GET"])
def login():
    # if the method is POST and Username is admin then
    # it will redirects to success url.
    if request.method == "POST" and request.form["Bream"] == "Bream" or request.form["Roach"] == "Roach" and request.form["Whitefish"] == "Whitefish" and  request.form["Parkki"] == "Parkki" and request.form["Perch"] == "Perch" and request.form["Pike"] == "Pike" and  request.form["Smelt"] == "Smelt":
        return redirect(url_for("success"))
    else:
        abort(403) #type of error
    # if the method is GET or username is not admin,
    # then it redirects to index method.
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

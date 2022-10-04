from my_app.api import app



app.env = "development"

if __name__=="__main__":
    app.run(debug=False)
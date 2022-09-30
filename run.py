from my_app.api import app



app.env = "development"

if __name__=="__main__":
    app.run(host = '0.0.0.0', port = '5000', debug = False)

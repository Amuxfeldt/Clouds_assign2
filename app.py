#clouds assignment 2 - Ex 1 --using Python, Flask
from flask import Flask
import numpy as np
import math

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>My numerical intergation microservice</p>"


@app.route("/integration/<lower>/<upper>")
def num_int(lower,upper):
    
    integral = numerical_integration(float(lower),float(upper))
    #print(integral)
    return f"<p>The result is: {integral}</p>"


def numerical_integration(lower, upper) :
    
    #defining function using lambda
    f = lambda x : abs(math.sin(x))

    f = np.vectorize(f)
    r = []

    for i in range(1,7):

        N = 10**i
        x = np.linspace(lower,upper,N)
        l = x[1] - x[0]

        y = f(x)
        area = y * l
        r.append(np.sum(area))
    
    return r

#if __name__ == "__main__":
#    app.run(port=8080)
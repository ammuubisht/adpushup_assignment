import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y, x_label,y_label, countries):
    plt.figure(figsize=(6,4))
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'o')
        plt.legend(countries)   
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    graph = get_graph()
    return graph 


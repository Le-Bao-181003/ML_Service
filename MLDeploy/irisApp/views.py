from django.shortcuts import render
from joblib import load
model = load('./saveModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']

        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        if y_pred[0] == 0:
            y_pred = 'Setosa'
        elif y_pred[0] == 1:
            y_pred = 'Versicolor'
        else:
            y_pred = 'Virginica'
        
        return render(request, 'main.html', {'result': y_pred})
    return render(request, 'main.html')

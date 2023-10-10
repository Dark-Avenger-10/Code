from math import exp

def predict(row, coefficients):
    yhat = coefficients[0]

    n = len(row)
    for i in range(n - 1):
        yhat = yhat + row[i] * coefficients[i+1]
    
    return 1/(1 + exp(-yhat))

def coefficients_sgd(dataset, n_epochs, l_rate):
    coef = [0.0 for i in range(len(dataset[0]))]

    for epoch in range(n_epochs):
        sum_error = 0

        for data in dataset:
            yhat = predict(data, coef)
            error = data[-1] - yhat
            sum_error = sum_error + error**2

            coef[0] = coef[0] + l_rate * error * yhat * (1 - yhat)
            for i in range(len(data)-1):
                coef[i+1] = coef[i+1] + l_rate * error * yhat * (1 - yhat) * data[i]
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return coef

# Calculate coefficients
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]
l_rate = 0.3
n_epoch = 100
coef = coefficients_sgd(dataset, n_epoch, l_rate)
print(coef)
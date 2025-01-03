import numpy as np

def forward(w, x, b):
    return w * x + b

def loss(w, x, b, y):
    n = len(x)
    total_loss = 0
    for i in range(n):
        val = ((forward(w, x[i], b) - y[i]) ** 2) / 2
        total_loss += val
    total_loss /= n
    return total_loss

def gradient_weight(w, x, y, b):
    n = len(x)
    total_gradient = 0
    for i in range(n):
        total_gradient += x[i] * (forward(w, x[i], b) - y[i])
    return (2 * total_gradient) / n

def gradient_bias(w, x, y, b):
    n = len(x)
    total_gradient = 0
    for i in range(n):
        total_gradient += (forward(w, x[i], b) - y[i])
    return (2 * total_gradient) / n

if __name__ == "__main__":
    w = 100  # Initial weight
    b = 100  # Initial bias
    lr = 0.007  # Learning rate
    x = [1, 2, 3, 4, 5]
    y = [101, 102, 103, 104, 105]  # True values

    epochs = 100000
    for i in range(epochs):
        # Calculate loss
        loss_final = loss(w, x, b, y)

        # Print loss every 1000 epochs
        if i % 1000 == 0:
            print(f"Epoch {i}, Loss: {loss_final}")

        # Update weight and bias using gradients
        w -= lr * gradient_weight(w, x, y, b)
        b -= lr * gradient_bias(w, x, y, b)

    print(f"Final weight: {w}, Final bias: {b}")






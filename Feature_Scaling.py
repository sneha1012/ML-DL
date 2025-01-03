#Types of Normalisation / feature scaling methods. Zscore means using the standard deviation of the feature and also average of each feature.
def zscore_normalise_features(X):
    """
    computes X, zscore normlaised by columns
    
    Args:
    X (ndarray (m,n)) : input data, m examples, n features (ndarray- 2D)

    Returns:
    X-norm(ndarray (m,n): input normalised by column)
    mu (ndarray (n,)): mean of each feature
    sigma(ndarray (n,)): standard deviation of each column
    
    """

    mu = np.mean(X, axis =0) #row-wise, Numpy treat axis = 0 as 1 dimenison and axis = 2 as 2 Dimension
    sigma = np.std(X, axis = 0)
    X_norm = (X - mu)/ sigma

    return (X_norm, mu, sigma)
    
    
    
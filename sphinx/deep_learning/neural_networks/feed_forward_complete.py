def feed_forward(X, weights):

    ''' STEP 1. calculate the dot product of X
    (shape of (50,3))
    and the weights of the first layer
    (shape of (3, 2))
    this results in an output shape of (50, 2)'''
    step1 = np.dot(X, weights[0])


    ''' STEP 2. apply the sigmoid function on the result
    (applying the sigmoid function on a 50x2 matrix outputs the same shape.
    '''
    step2 = sigmoid(step1)


    ''' STEP 3. append an extra 1 for the bias to the result
    (this results in a 50x3 matrix)'''
    step3 = np.hstack([step2, np.ones((step2.shape[0], 1))])


    ''' STEP 4. calculate the dot product of X (from step 3)
    (shape of (50, 3))
    and the weights of the second layer
    (shape of (3, 1)). This results in an output shape of (50, 1)'''
    step4 = np.dot(step3, weights[1])


    ''' STEP 5. apply the sigmoid function on the result'''
    step5 = sigmoid(step4)

    
    ''' STEP 6. return all intermediate results'''
    return step2, step5

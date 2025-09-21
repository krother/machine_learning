Entropy is a measure of the uncertainty associated with a given distribution q(y).

H(q) = log(2)  # for half-half-case, measured in bits

If we knew the distribution:

H(q) = -sum{q(y_c) * log(q(y_c))}   over all classes

but we do not know the distribution. We approximate q(y) by p(y):

Hp(q) = -sum{q(y_c) * log(p(y_c))}   cross-entropy
--------------
Hp(q) - H(q) >= 0 --> Kullback-Leibler Divergence, measures dissimilarity of distributions


We want to find the best p(y) so that the cross-entropy gets minimal.

Calculate it pointwise

yi = 1: log(p)
yi = 0: log(1-p)

Hp(q) = - 1/N sum_N{yi*log(p(yi)) + (1-yi)*log(1-p(yi))}

Theory background on Entropy and Kullback-Leibler Divergence:
https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a

OvR
Multinomial with Softmax

https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression

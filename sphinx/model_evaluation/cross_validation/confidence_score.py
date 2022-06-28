
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.utils import resample

X, y = load_iris(True)
eighty_percent_split = int(len(X)*0.8)

m = LogisticRegression()

boots = []
for i in range(1000):
    # Resample the original data to create a "new" dataset
    Xb, yb = resample(X, y)
    
    # Split the data into training and validation set
    Xb_train = Xb[:eighty_percent_split]
    yb_train = yb[:eighty_percent_split]
    Xb_validation = Xb[eighty_percent_split:]
    yb_validation = yb[eighty_percent_split:]

    # Fit the model and calculate the validation score
    m.fit(Xb_train, yb_train)
    score = m.score(Xb_validation, yb_validation)
    boots.append(score)
    print(i, score)

# get percentiles for 90% confidence
boots.sort()
ci80 = boots[100:-100]
print(f"80% confidence interval: {ci80[0]:5.2} -{ci80[-1]:5.2}")
ci90 = boots[50:-50]
print(f"90% confidence interval: {ci90[0]:5.2} -{ci90[-1]:5.2}")
ci95 = boots[25:-25]
print(f"95% confidence interval: {ci95[0]:5.2} -{ci95[-1]:5.2}")
ci99 = boots[5:-5]
print(f"99% confidence interval: {ci99[0]:5.2} -{ci99[-1]:5.2}")

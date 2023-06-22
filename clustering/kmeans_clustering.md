:

K-Means from Scratch
:::

> Implement the **k-means clustering** algorithm from scratch.
>
> **Step 1**

> Generate data for 200 points with two features x1 and x2:
>
> from sklearn.datasets import make_blobs
> X, _ = make_blobs(n_features=2, n_samples=200,centers=2, random_state=42)
> ```
>
> Visualize these points as a scatterplot.
>
> We want to group the points by proximity.
>
> **Step 2**
>
> Assign the points randomly to two clusters *\"red\"* and *\"blue*\"
> e.g. with:
>
> clusters = ["red", "blue"] * 100
> ```
>
> **Step 3**
>
> Calculate the mean for both x1 and x2.
>
> **Step 4**
>
> Calculate the mean x1/x2 for blue and red points separately. We will
> call these mean points `blue_center` and `red_center`.
>
> **Step 5**
>
> Calculate the euclidean distance from each point to `blue_center` and
> `red_center`.
>
> **Step 6**
>
> Re-label the points. Those points closer to `blue_center` shall be
> labeled `blue`, those closer to `red_center` shall be labeled `red`.
>
> **Step 7**
>
> Repeat steps 2-4 three times.
>
> **Step 8**
>
> The final assignment of the labels `blue` and `red` is the k-means
> clustering.
>
> Draw another scatterplot, using these colors.
>

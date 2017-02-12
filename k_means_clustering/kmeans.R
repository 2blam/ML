# kmeans

setwd("~/Documents/GitHub/ML/k_means_clustering")

#read the dataset
dataset = read.csv("Mall_Customers.csv")
X = dataset[4:5]

#elbow method
set.seed(6)
wcss = vector()
for (i in 1:10){
  wcss[i] = sum(kmeans(X, i)$withinss)
}

# type "b" === both, i.e. line + point
plot(1:10, wcss, type="b", main=paste("Cluster of clients"), xlab="Number of clusters", ylab="WCSS")
#optimal number of clusters = 5

# apply kmeans
set.seed(29)
kmeans = kmeans(X, 5, iter.max=300, nstart=10)

# visualize
library(cluster)
clusplot(X, 
         kmeans$cluster, 
         lines=0, 
         shade=TRUE, 
         color=TRUE, 
         labels=2, 
         plotchar=FALSE, 
         span=TRUE, 
         main=paste("Clusters of clients"), 
         xlab="Annual income",
         ylab="Spending score")
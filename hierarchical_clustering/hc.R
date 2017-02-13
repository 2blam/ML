# hierarchical clustering by 2blam

# set working directory
setwd("~/Documents/Git/ML/hierarchical_clustering")

#read the dataset
dataset = read.csv("Mall_Customers.csv")
X = dataset[4:5]

#dendrogram
dendrogram = hclust(dist(X, method="euclidean"), method="ward.D")
plot(dendrogram, 
     main=paste("Dendrogram"),
     xlab="Customers",
     ylab="Euclidean distances")

#optimal clusters = 5

# fit hc
hc = hclust(dist(X, method="euclidean"), method="ward.D")
y_hc = cutree(hc, k=5) #cut tree with 5 groups

library(cluster)
clusplot(X, 
         y_hc, 
         lines=0, 
         shade=TRUE, 
         color=TRUE, 
         labels=2, 
         plotchar=FALSE, 
         span=TRUE, 
         main=paste("Clusters of clients"), 
         xlab="Annual income",
         ylab="Spending score")

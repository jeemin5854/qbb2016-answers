library("ggplot2")


# Ward Hierarchical Clustering
mydata <-read.delim("~/qbb2016-answers/week11-answers/hema_data.txt", header = T)
rownames(mydata) <- mydata$gene
mydata <- mydata[, -c(1)]

mydata <- mydata[,c(1,5,6,4,3,2)]



mydata <- scale(mydata) # standardize variables
d <- dist(mydata, method = "euclidean") # distance matrix
fit <- hclust(d, method="complete") 
plot(fit) # display dendogram
groups <- cutree(fit, k=5) # cut tree into 5 clusters
# draw dendogram with red borders around the 5 clusters 
#rect.hclust(fit, k=5, border="red")
png("~/qbb2016-answers/week11-answers/heatmapcelltype.png", width=6, height = 3.5 , units= "in", res=1200, pointsize = 5)

heatmap(mydata, Rowv= fit$order)
dev.off()
heatmap(mydata, Rowv= fit$order, Colv =NA)



#2
library("ggplot2")


# Ward Hierarchical Clustering
mydata <-read.delim("~/qbb2016-answers/week11-answers/hema_data.txt", header = T)
rownames(mydata) <- mydata$gene
mydata <- mydata[, -c(1)]

mydata <- mydata[,c(1,5,6,4,3,2)]


wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata, centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")
# K-Means Cluster Analysis
fit <- kmeans(mydata, 5) # 5 cluster solution
# get cluster means 
aggregate(mydata,by=list(fit$cluster),FUN=mean)
# append cluster assignment
mydata <- data.frame(mydata, fit$cluster)
mydata$color[mydata$fit.cluster ==1] <- "green"
mydata$color[mydata$fit.cluster ==2] <- "red"
mydata$color[mydata$fit.cluster ==3] <- "blue"
mydata$color[mydata$fit.cluster ==4] <- "orange"
mydata$color[mydata$fit.cluster ==5] <- "yellow"
ggplot(mydata, aes(x= mydata$CFU, y = mydata$poly)) + geom_point(color = mydata$color, alpha = .5)



#3
# Ward Hierarchical Clustering
mydata <-read.delim("~/qbb2016-answers/week11-answers/hema_data.txt", header = T)
rownames(mydata) <- mydata$gene
mydata <- mydata[, -c(1)]
mydata <- mydata[,c(1,5,3,2)]
df_new <- mydata

for (i in 1:nrow(mydata)){
  temp_mydata <- data.frame()
  row_num <- 1
  for (ii in 1:ncol(mydata)){
    temp_mydata[row_num, 1] <- mydata[i,ii]
    row_num = row_num + 1
  }
  temp_mydata$V2 <- c("early", "early", "late", "late")
  col_mean <- mean(temp_mydata[,1])
  if (temp_mydata[1,1] == col_mean){
    df_new[i, ncol(mydata) + 1 ] <- .99
    df_new[i, ncol(mydata) +2] <- 0
    
  }
  else {
  a <- t.test(temp_mydata$V1~temp_mydata$V2)
  df_new[i, ncol(mydata) + 1] <- a$p.value
  b <- data.frame(a$estimate)
  late_val <- b[2,]
  early_val <- b[1,]
  diff <- log2(late_val/early_val)
  df_new[i, ncol(mydata) +2] <- diff
  }
}
colnames(df_new)[ncol(df_new) -1 ] <- "pvalue"
colnames(df_new)[ncol(df_new)  ] <- "diff"

df_sig <- df_new[df_new$pvalue < 0.05,]
p.adjust(df_new$pvalue)

write.table(df_sig, "~/qbb2016-answers/week11-answers/sig_TABLE.txt", row.names = T, col.names = T, sep = "\t", quote = F)

a <- data.frame(rownames(df_sig)) 
write.table(a, "~/qbb2016-answers/week11-answers/sig_genes.txt", row.names = F, col.names = F, sep = "\t", quote = F)



#4

#Panther 
#make a list of all cluster 5 genes
#convert genes to ID
#do a Panther on the gene IDs
#The end!


library("ggplot2")


# Ward Hierarchical Clustering
mydata <-read.delim("~/qbb2016-answers/week11-answers/hema_data.txt", header = T)
rownames(mydata) <- mydata$gene
mydata <- mydata[, -c(1)]

mydata <- mydata[,c(1,5,6,4,3,2)]


wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata, centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")
# K-Means Cluster Analysis
fit <- kmeans(mydata, 5) # 5 cluster solution
# get cluster means 
aggregate(mydata,by=list(fit$cluster),FUN=mean)
# append cluster assignment
mydata <- data.frame(mydata, fit$cluster)
mydata$color[mydata$fit.cluster ==1] <- "green"
mydata$color[mydata$fit.cluster ==2] <- "red"
mydata$color[mydata$fit.cluster ==3] <- "blue"
mydata$color[mydata$fit.cluster ==4] <- "orange"
mydata$color[mydata$fit.cluster ==5] <- "yellow"
ggplot(mydata, aes(x= mydata$CFU, y = mydata$poly)) + geom_point(color = mydata$color, alpha = .5)


mydata <- mydata[mydata$fit.cluster ==5,] 
mydata$id <- rownames(mydata)
mydata <- mydata[, c(7,9)]
df_sig$id <- rownames(df_sig)
clustsig <- merge(mydata, df_sig, by = "id")
write.table(clustsig, "~/qbb2016-answers/week11-answers/cluster5.txt", row.names = T, col.names = T, sep = "\t", quote = F)


write.table(cluster5list, "~/qbb2016-answers/week11-answers/cluster5.txt", row.names = T, col.names = T, sep = "\t", quote = F)
listGO <- goProfiles::basicProfile(genelist = GOlist)
goProfiles::plotProfiles(listGO, aTitle = "GO analysis")

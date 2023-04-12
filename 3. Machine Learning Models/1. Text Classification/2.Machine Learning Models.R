library(caret) #used to train models
library(caret)#machine learning modeling
library(doMC)
registerDoMC(cores = 4)

set.seed(2015)

#reading in training and test set
setwd("~/Documents/Text Classification - Resumes/1. Data")

df <- read.csv("TDM.csv")

inBuild <- createDataPartition(y = df$target,p=0.7, list=FALSE)
test <- df[-inBuild,]
train <- df[inBuild,]




#######################################
#Training Methodology

fitControl <- trainControl(## 10-fold CV
        method = "repeatedcv",
        number = 10,
        ## repeated ten times
        repeats = 10)



#######################################
#Level 1 Models - on training data

model.1 <- train(target ~ ., 
                 method="xgbTree",
                 trControl = fitControl, 
                 data = train)


model.2 <- train(target ~ ., 
                 method="rf", 
                 trControl = fitControl,
                 data = train)

model.3 <- train(target ~ ., 
                 method="knn", 
                 trControl = fitControl,
                 data = train)

model.4 <- train(target ~ ., 
                 method="svmLinear", 
                 trControl = fitControl,
                 data = train)

#Creating new data based for ensemble models
train$model.1 <- predict(model.1, train)
train$model.2 <- predict(model.2, train)
train$model.3 <- predict(model.3, train)
train$model.4 <- predict(model.4, train)




#######################################
#Level 1 - Ensemble Models - for greater accuracy

#Training ensemble models on the training set with other model's predictors
ensemble.1 <- train(target ~ ., 
                    method="xgbTree", 
                    trControl = fitControl,
                    data = train)

ensemble.2 <- train(target ~ ., 
                    method="rf", 
                    trControl = fitControl,
                    data = train)

ensemble.3 <- train(target ~ ., 
                    method="knn", 
                    trControl = fitControl,
                    data = train)

ensemble.4 <- train(target ~ ., 
                    method="svmLinear", 
                    trControl = fitControl,
                    data = train)

train$ensemble.1 <- predict(ensemble.1, train)
train$ensemble.2<- predict(ensemble.2, train)
train$ensemble.3 <- predict(ensemble.3, train)
train$ensemble.4 <- predict(ensemble.4, train)




#######################################
#Level 2 - Ensemble Models

final.ensemble <- train(target ~ ., 
                        method="xgbTree",
                        trControl = fitControl,
                        data = train)
final.ensemble


#######################################
#Accessing Model Accuracy on test data
test$model.1 <- predict(model.1, test)
test$model.2 <- predict(model.2, test)
test$model.3 <- predict(model.3, test)
test$model.4 <- predict(model.4, test)
test$ensemble.1 <- predict(ensemble.1, test)
test$ensemble.2 <- predict(ensemble.2, test)
test$ensemble.3 <- predict(ensemble.3, test)
test$ensemble.4 <- predict(ensemble.4, test)
test$final.ensemble <- predict(final.ensemble, test)



#Out of Sample Error: 1) Predict on test set and examine confusion matrix
confusionMatrix(test$target, test$model.1)
confusionMatrix(test$target, test$model.2)
confusionMatrix(test$target, test$model.3)
confusionMatrix(test$target, test$model.4)

confusionMatrix(test$target, test$ensemble.1)
confusionMatrix(test$target, test$ensemble.2)
confusionMatrix(test$target, test$ensemble.3)
confusionMatrix(test$target, test$ensemble.4)

confusionMatrix(test$target, test$final.ensemble)

#######################################
#Accessing Model Accuracy on complete dataset
df$model.1 <- predict(model.1, df)
df$model.2 <- predict(model.2, df)
df$model.3 <- predict(model.3, df)
df$model.4 <- predict(model.4, df)
df$ensemble.1 <- predict(ensemble.1, df)
df$ensemble.2 <- predict(ensemble.2, df)
df$ensemble.3 <- predict(ensemble.3, df)
df$ensemble.4 <- predict(ensemble.4, df)
df$final.ensemble <- predict(final.ensemble, df)


confusionMatrix(df$target, df$model.1)
confusionMatrix(df$target, df$model.2)
confusionMatrix(df$target, df$model.3)
confusionMatrix(df$target, df$model.4)

confusionMatrix(df$target, df$ensemble.1)
confusionMatrix(df$target, df$ensemble.2)
confusionMatrix(df$target, df$ensemble.3)
confusionMatrix(df$target, df$ensemble.4)

confusionMatrix(df$target, df$final.ensemble)


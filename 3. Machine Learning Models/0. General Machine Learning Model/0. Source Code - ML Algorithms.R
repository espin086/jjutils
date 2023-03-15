library(caret) #used to train models
library(doMC)
registerDoMC(cores = 4)

#######################################
#Training Methodology
set.seed(2015)
fitControl <- trainControl(## 10-fold CV
        method = "repeatedcv",
        number = 3,
        ## repeated ten times
        repeats = 10)


#######################################
#Machine Learning Models

#List of models to use based on top algorithms used in Kaggle Competitions
#model.list <- c("xgbTree", "rf", "nnet" , "glm")

#for (i in 1:length(model.list)){
                #cat(model.list[i]) <- train(target ~ ., 
                                 #method=model.list[i],
                                 #trControl = fitControl, 
                                 #data = training)
#}


run.xgbTree <- function(training, target){
        xgbTree <- train(target ~ ., 
                         method="xgbTree",
                         trControl = fitControl, 
                         data = training)  
        xgbTree <- list(xgbTree)
        return(scored)
}

run.models <- function(training, target){


        
        rf <- train(target ~ ., 
                         method="rf",
                         trControl = fitControl, 
                         data = training)
        
        nnet <- train(target ~ ., 
                         method="nnet",
                         trControl = fitControl, 
                         data = training)
        
        glm <- train(target ~ ., 
                      method="glm",
                      trControl = fitControl, 
                      data = training)
        
        scored <- list(xgbTree, rf , nnet, glm)
        return(scored)

}




#####################################################
#Sub Routines
#####################################################

#Removing zerio variance function
remove.zero <- function(dataframe){
        library(caret)#used for removing zero variance
        nzv <- nearZeroVar(dataframe, saveMetrics= TRUE)
        nzv<-nzv[nzv$nzv=="TRUE",]
        nzv<-row.names(nzv)
        myvars <- names(dataframe) %in% nzv
        return(dataframe)
}
#Center and scaling
center.scale <- function(dataframe){
        library(MASS) #used for center and scaling
        #Centering and scaling numberical data
        ind.n <- sapply(dataframe, is.numeric)
        dataframe[ind.n] <- lapply(dataframe[ind.n], scale)
        return(dataframe)
}
#Performing MICE Imputation
mice.imp <- function(dataframe){
        library(mice)
        mice_mod <- mice(dataframe, method='rf') 
        dataframe <- complete(mice_mod)
        return(dataframe)
}
#Hot Encoding all factor variables
hot.encode <- function(dataframe){
        dataframe <- model.matrix(~ ., data=dataframe, 
                     contrasts.arg = lapply(dataframe[,sapply(dataframe, is.factor)], contrasts, contrasts=FALSE))
        return(dataframe)
        
}

#####################################################
#Main Function
#####################################################

prep.data <- function(dataframe){
        
        #Removing data with zero variance
        dataframe.1 <- remove.zero(dataframe)
        #Center Scale
        dataframe.2 <- center.scale(dataframe)
        #Mice Imputation
        dataframe.3 <- mice.imp(dataframe)
        #Hot Encode factors
        #dataframe.4 <- hot.encode(dataframe)
        #Returning dataframe
        results <- list(dataframe.1, dataframe.2, dataframe.3)
        return(results)
        
}



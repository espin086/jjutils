library(reshape)


#Function for preparing data = prep.data
source("/Users/jjespinoza/Documents/my-toolbox/3. Machine Learning Models/0. Source Code - Prep Data.R")

#Function for Machine Learning = Models
source("/Users/jjespinoza/Documents/my-toolbox/3. Machine Learning Models/0. Source Code - ML Algorithms.R")

setwd("/Users/jjespinoza/Documents/Kaggle - Titanic Disaster/2. Data")
df <- read.csv("train (1).csv")

########################################
#PREPARING DATA USING SOURCE CODE
########################################

#Identifying target variables
target <- df["Survived"]
#Removing target and useless features
myvars <- names(df) %in% c("PassengerId", "Survived", "Name", "Ticket", "Cabin") 
df <- df[!myvars]
#Correcting variable types
df$Pclass <- as.factor(df$Pclass)

##############
#Feature engineering
df <- prep.data(dataframe = df, target = Survived)

#Merging target with features
df <- cbind(df, target)
#Specifiying target variable
df$Survived <- as.factor(as.character(df$Survived))
#Chaning name to identify target
df <- rename(df, c(Survived="target"))


########################################
#BUILDING MACHINE LEARNING MODELS
########################################

models <- run.models(df, df)




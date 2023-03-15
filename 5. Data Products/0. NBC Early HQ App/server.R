library(shiny)
library(UsingR)
library(caret)

#Reading in the training
setwd("~/Documents/my-shiny-tools/1. Prediction App/")
df <- read.csv("regressionraw_2016_03.csv")

#Removing film title & interaction terms
myvars <- names(df) %in% c("Film.Title", "Box...Days.to.HQ") 
df.clean <- df[!myvars]

#Building Prediction Model
fit.knn <- train(WW210 ~.,method="knn",data=df.clean)

#############################
#Prediction Function

Days.to.HQ <- 10
WW.Box <- 10000
Has.CAM. <- 1
A <- 1
Animation <- 1
Adventure <- 0
Comedy <- 0
Drama <- 0
Romantic.Comedy <- 0
Horror.Thriller <- 0
PG.13 <- 0
R <- 1

inputs <- data.frame(Days.to.HQ, WW.Box, Has.CAM., A, Animation, Adventure, Comedy, Drama, Romantic.Comedy, Horror.Thriller, PG.13, R )


#Creating a function that takes inputs and uses fitted model to predict outcome
model <- function(x) {predict(fit.knn, x)}


shinyServer(
        function(input, output){
                
                output$DaystoHQ <- renderPrint({input$DaystoHQ})
                output$Genre <- renderPrint({input$Genre})
                
                output$Prediction <- renderPrint(model(inputs))
                
                
        }
)
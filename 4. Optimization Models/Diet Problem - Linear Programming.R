########################################
#Feeding Babies

#Importing data from Github

library(RCurl)
library(foreign)


url <- "https://raw.githubusercontent.com/espin086/data-dad/master/Optimizing%20the%20Feeding%20of%20Babies/Baby%20Food.csv"
baby.food <- getURL(url)                
baby.food <- read.csv(textConnection(baby.food), header = TRUE, skip =1)
###################################################################
#Setting up Linear Programming Problem

#######################
#Objective Function
cost <- c(baby.food[,2])

#######################
#Constraints

#1. Calories: 1 month old female needs 438 calories per day.
rhs.constraint<- c(438)*-1
lhs.constraint <- rbind(c(baby.food[,3])*-1)

#2. Carbs: From 0-6 month olds need at least 60 carbs per day
rhs.carb.constraint <- c(60)*-1
rhs.constraint <- c(rhs.constraint, rhs.carb.constraint)

lhs.carb.constraint <- c(baby.food[,7])*-1
lhs.constraint <- rbind(lhs.constraint, lhs.carb.constraint)


#Protein: From 0-6 months old need at least 9.1 grams of protein
rhs.protein.constraint <- c(9.1)*-1
rhs.constraint <- c(rhs.constraint, rhs.protein.constraint)

lhs.protein.constraint <- c(baby.food[,10])*-1
lhs.constraint <- rbind(lhs.constraint, lhs.protein.constraint)

#Vitamin A: Goal is to hit 100% Vitamin A; check with Dr. if % on product matches needs 0-6 month old
rhs.vitaminA.constraint <- c(1)*-1
rhs.constraint <- c(rhs.constraint, rhs.vitaminA.constraint)

lhs.vitaminA.constraint <- c(baby.food[,11])*-1
lhs.constraint <- rbind(lhs.constraint, lhs.vitaminA.constraint)

#Vitamin C: Goal is to hit 100% Vitamin C; check with Dr. if % on product matches needs 0-6 month old
rhs.vitaminC.constraint <- c(1)*-1
rhs.constraint <- c(rhs.constraint, rhs.vitaminC.constraint)

lhs.vitaminC.constraint <- c(baby.food[,12])*-1
lhs.constraint <- rbind(lhs.constraint, lhs.vitaminC.constraint)


#######################
#Solving the Linear Programming Problem
library(linprog)
answer <- solveLP(cost, rhs.constraint, lhs.constraint, maximum = FALSE)

answer$opt
answer$solution
answer$con

#######################
#Visualizing Solution
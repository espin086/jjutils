
################################################################


#Importing data from Github

library(RCurl)
library(foreign)


url <- "https://docs.google.com/spreadsheets/d/1Okuj7zW1yTibQ4jK_3eppBis7OYVp0LaFr3qXNeTbCs/pub?output=csv"
cost.reach <- getURL(url)                
cost.reach <- read.csv(textConnection(cost.reach), header = TRUE, skip =0)


url2 <- "https://docs.google.com/spreadsheets/d/1xREig0Fmk7S7g9OxSVpD-o3cAO3ZzHofIwU289AHs00/pub?output=csv"
target <- getURL(url2)                
target <- read.csv(textConnection(target), header = TRUE, skip =0)


################################################################

#######################
#Objective Function
cost <- c(cost.reach[,2])

#######################
#Constraints

#1. The goal is to reach 24 million boys cheaply, while meeting all other goals.
rhs.constraint<- c(target[1,2])*-1
lhs.constraint <- rbind(c(cost.reach[,3])*-1)


#2. The goal is to reach 18 million women cheaply, while meeting all other goals.
rhs.woman.constraint<- c(target[2,2])*-1
rhs.constraint <- rbind(rhs.constraint, rhs.woman.constraint)
lhs.woman.constraint <- rbind(c(cost.reach[,4])*-1)
lhs.constraint <- rbind(lhs.constraint, lhs.woman.constraint)

#3. The goal is to reach 24 million men cheaply, while meeting all other goals.
rhs.men.constraint<- c(target[3,2])*-1
rhs.constraint <- rbind(rhs.constraint, rhs.men.constraint)
lhs.men.constraint <- rbind(c(cost.reach[,5])*-1)
lhs.constraint <- rbind(lhs.constraint, lhs.men.constraint)

#######################
#Solving the Linear Programming Problem
library(linprog)
answer <- solveLP(cost, rhs.constraint, lhs.constraint, maximum = FALSE)


answer$opt
answer$solution
answer$con

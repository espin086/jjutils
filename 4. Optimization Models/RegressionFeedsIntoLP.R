######################################################
#The following code performs a marketing mix model
        #1) Measures marketing effectiveness
        #2) Uses effective measures along with costs in optimization
######################################################

#Importing marketing and sales data
setwd("~/Documents/Primer on Linear Programming/2. Simple Example - Data and Code")
df <- read.csv("advertising.csv")

model <- lm(Sales ~ TV + Radio, data = df) #Modeling marketing's impact on sales
summary(model)


######################################################
#1) Establishing the 'Base' optimization
library(linprog)

#Objective - maximize sales by pulling the ratio & TV levers
cvec <- c(Radio = model[[1]][[3]], 
          TV = model[[1]][[2]])  

## Constraints (quasi-fix factors)
bvec <- c( RadioBudget = 23.275,
           TVBudget = 147.04,
           TotalBudget = 170.315) #Add or remove 3.65 for marketing mix problem
bvec

## Needs of Production activities
Amat <- matrix(0, length(bvec), length(cvec))
rownames(Amat) <- names(bvec)
colnames(Amat) <- names(cvec)


#specifying LHS of radio budget constraint
Amat["RadioBudget", "Radio"] <- 1
Amat["RadioBudget", "TV"] <- 0

#specifying LHS of TV budget constraint
Amat["TVBudget", "Radio"] <- 0
Amat["TVBudget", "TV"] <- 1

#specifying LHS of Total budget constraint
Amat["TotalBudget", "Radio"] <- 1
Amat["TotalBudget", "TV"] <- 1

Amat

#Solving the linear program
lp <- solveLP(cvec, bvec, Amat, maximum = TRUE )
lp$solution
lp$opt + model[[1]][[1]] #Adding intercept value to model results

#As we can see when we use the mean inputs we get the mean output from the data from the optimization results
summary(df)

######################################################
#Q: You mention to the marketing department that Radio 3 times as effective as TV, so they ask you what would happen if they kept the total budget the same but let the Radio budget go up by 20%?


######################################################
#Q: You mention to the marketing department that Radio 3 times as effective as TV, so they ask you what would happen if they kept the total budget the same but let the Radio budget go up by 20%?

bvec.2 <- c( RadioBudget = 23.275*1.2,
           TVBudget = 147.04,
           TotalBudget = 170.315)

bvec.2
bvec

#A we see that sales goes up by 5% and there is a rebalancing inputs  
lp.2 <- solveLP(cvec, bvec.2, Amat, maximum = TRUE )
lp.2$solution
lp.2$opt + model[[1]][[1]]
summary(df)


######################################################
#Q: It seems that other companies have noticed the effectiveness of radio ads on their sales and started purchasing additional ads. Radio stations faced with rising demand decide to double their prices, what is our response to maximize sales?

## Needs of Production activities
Amat.2 <- matrix(0, length(bvec), length(cvec))
rownames(Amat.2) <- names(bvec)
colnames(Amat.2) <- names(cvec)

#specifying LHS of radio budget constraint
Amat.2["RadioBudget", "Radio"] <- 2
Amat.2["RadioBudget", "TV"] <- 0

#specifying LHS of TV budget constraint
Amat.2["TVBudget", "Radio"] <- 0
Amat.2["TVBudget", "TV"] <- 1

#specifying LHS of Total budget constraint
Amat.2["TotalBudget", "Radio"] <- 2
Amat.2["TotalBudget", "TV"] <- 1

Amat.2

#We continue to invest in radio but less than before our sales decrease by 14% as our budget doesn't go as far as it used to
lp.3 <- solveLP(cvec, bvec.2, Amat.2, maximum = TRUE )
lp.3$solution
lp.3$opt + model[[1]][[1]]
summary(df)

######################################################
#Q: TV stations realize that the popularity of radio is increasing and cannibalizing their business, so they run a few focus groups and find out that people love ads with babies and puppies in them.  A year later you analyze the effectiveness of TV adds and see that TV ads are now driving 150% more sales than they used to, the new content has made TV ads more effective.  Given the current market what should be done and how is the business impacted?

cvec.2 <- c(Radio = model[[1]][[3]], 
          TV = model[[1]][[2]]*2.50) 
cvec.2

lp.4 <- solveLP(cvec.2, bvec.2, Amat.2, maximum = TRUE )
lp.4$solution
lp.4$opt + model[[1]][[1]]

summary(df)


######################################################
#Q: The CMO of marketing is happy with the job you've done so far and asks you whether or not the company should diversify it's adverising to include newspapers.  He connects you with IT who provides you marketing data on newspapers and tells you that he wants to increase the budget by 25% to accomodate the new tactic.

model.2 <- lm(Sales ~ TV + Radio + Newspaper, data = df) 
summary(model.2)

#A: You run the model and find that newspapers do not life sales in a statistically significant manner.  However, you realize that if there is extra budget, it may be wise to quantify what impact the increased budget will have on on sales given existing marketing channels (TV, Radio)

bvec.3 <- c( RadioBudget = 23.275*1.2*1.25,
             TVBudget = 147.04*1.25,
             TotalBudget = 170.315*1.25)

lp.5 <- solveLP(cvec.2, bvec.3, Amat.2, maximum = TRUE )
lp.5$opt + model[[1]][[1]]
lp.5$solution
summary(df)

#A Part 2: You bring back the updated results and recommendations and the CMO is happy to avert wasteful spending on newspapers and instead follows your recommendations proceeding to another great year
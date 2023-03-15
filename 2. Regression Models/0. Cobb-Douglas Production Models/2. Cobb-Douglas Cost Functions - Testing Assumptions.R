library(miscTools)

############################################
#Estimation and analysis of Cobb-Douglas Cost Function

#This production function violates the homogeneity assumption
costCD <- lm(log(cost) ~ log(pProps) + log(pDirector) + log(pActors) + log(qTotalView), data = dat)
summary(costCD)

#The following variable transformation imposes homogeneity by normalizing by actors
costCDHom <- lm(log(cost/pActors) ~ log(pProps/pActors) + log(pDirector/pActors) + log(qTotalView), data = dat)
summary(costCDHom)

#The following variable transformation imposes homogeneity by normalizing by props
costCDHomCap <- lm(log(cost/pProps) ~ log(pDirector/pProps) + log(pActors/pProps) + log(qTotalView), data = dat)
summary(costCDHomCap)
    
############################################
#Checking Assumption of Homogeneity in Input Prices

#Test for homogeneity in input prices
library( "car" )
#if test below have p-values greater than .10 than we do no contradict linear homogenerity in input prices, this is a good thing
linearHypothesis( costCD, "log(pProps) + log(pDirector) + log(pActors) = 1"  )
lrtest( costCDHom, costCD )

############################################
#Checking Assumption of Concavity of Input Prices with regression WITHOUT homogeneity imposed

dat$costCD <- exp(fitted(costCD))

#simplifying calcs by defining short-cuts for coefficients
cProps <- coef(costCD)["log(pProps)"]
cDirector <- coef(costCD)["log(pDirector)"]
cActors <- coef(costCD)["log(pActors)"]

#Calculating the Hessian Matrix
hPropsProps <- cProps * ( cProps - 1 ) * dat$costCD / dat$pProps^2
hDirectorDirector <- cDirector * ( cDirector - 1 ) * dat$costCD / dat$pDirector^2
hActorsActors <- cActors * ( cActors - 1 ) * dat$costCD / dat$pActors^2
hPropsDirector <- cProps * cDirector * dat$costCD / ( dat$pProps * dat$pDirector )
hPropsActors <- cProps * cActors * dat$costCD / ( dat$pProps * dat$pActors )
hDirectorActors <- cDirector * cActors * dat$costCD / ( dat$pDirector * dat$pActor )

#Producing the Hessian Matrix for the first observation

hessian <- matrix(NA, nrow = 3, ncol = 3)
hessian[1,1] <- hPropsProps[1]
hessian[2,2] <- hDirectorDirector[1]
hessian[3,3] <- hActorsActors[1]
hessian[1,2] <- hessian[2,1] <- hPropsDirector[1]
hessian[1,3] <- hessian[3,1] <- hPropsActors[1]
hessian[2,3] <- hessian[3,2] <- hDirectorActors[1]

print(hessian)

#Testing for concavity (aka semidefinteness) on first observation
semidefiniteness( hessian, positive = FALSE )#if false then we don't have 

#Testing for concavity (aka semidefinteness) on all observations
dat$concaveCD <- NA
for( obs in 1:nrow( dat ) ) {
        hessianLoop <- matrix( NA, nrow = 3, ncol = 3 )
        hessianLoop[ 1, 1 ] <- hPropsProps[obs]
        hessianLoop[ 2, 2 ] <- hDirectorDirector[obs]
        hessianLoop[ 3, 3 ] <- hActorsActors[obs]
        hessianLoop[ 1, 2 ] <- hessianLoop[ 2, 1 ] <- hPropsDirector[obs]
        hessianLoop[ 1, 3 ] <- hessianLoop[ 3, 1 ] <- hPropsActors[obs]
        hessianLoop[ 2, 3 ] <- hessianLoop[ 3, 2 ] <- hDirectorActors[obs]
        dat$concaveCD[obs] <- semidefiniteness( hessianLoop, positive = FALSE ) }
sum( dat$concaveCD )



############################################
#Checking Assumption of Concavity of Input Prices with regression WITH homogeneity imposed
dat$costCDHom <- exp( fitted( costCDHom ) ) * dat$pActors

chProps <- coef( costCDHom )[ "log(pProps/pActors)" ]
chDirector <- coef( costCDHom )[ "log(pDirector/pActors)" ]
chActors <- 1 - chProps - chDirector


#Calculating the Hessian Matrix
hhPropsProps <- chProps * ( chProps - 1 ) * dat$costCD / dat$pProps^2
hhDirectorDirector <- chDirector * ( chDirector - 1 ) * dat$costCD / dat$pDirector^2
hhActorsActors <- chActors * ( chActors - 1 ) * dat$costCD / dat$pActors^2
hhPropsDirector <- chProps * chDirector * dat$costCD / ( dat$pProps * dat$pDirector )
hhPropsActors <- chProps * chActors * dat$costCD / ( dat$pProps * dat$pActors )
hhDirectorActors <- chDirector * chActors * dat$costCD / ( dat$pDirector * dat$pActor )

#New Hessian Matrix
hessianHom <- matrix( NA, nrow = 3, ncol = 3 )
hessianHom[ 1, 1 ] <- hhPropsProps[1]
hessianHom[ 2, 2 ] <- hhDirectorDirector[1]
hessianHom[ 3, 3 ] <- hhActorsActors[1]
hessianHom[ 1, 2 ] <- hessianHom[ 2, 1 ] <- hhPropsDirector[1]
hessianHom[ 1, 3 ] <- hessianHom[ 3, 1 ] <- hhPropsActors[1]
hessianHom[ 2, 3 ] <- hessianHom[ 3, 2 ] <- hhDirectorActors[1]
print( hessianHom )

semidefiniteness( hessianHom, positive = FALSE )#if false then we don't have 

#This shows that concavity was not violated any any observation
dat$concaveCDHom <- NA
for( obs in 1:nrow( dat ) ) {
       hessianPart <- matrix( NA, nrow = 2, ncol = 2 )
       hessianPart[ 1, 1 ] <- hhPropsProps[obs]
       hessianPart[ 2, 2 ] <- hhDirectorDirector[obs]
       hessianPart[ 1, 2 ] <- hessianPart[ 2, 1 ] <- hhPropsDirector[obs]
       dat$concaveCDHom[obs] <- semidefiniteness( hessianPart, positive = FALSE ) }
sum(!dat$concaveCDHom) #Shows that concavity was not violated at any single observation


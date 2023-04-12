library(car)
library(datasets)
fit <- lm(Fertility ~ ., data=swiss)

############################################
#function for ols diagnostics
ols.diagnostics <- function(ols.model){
        
        #############################################
        #The basic tool for diagnosing regression models are residual plots
        plot(ols.model, which = 1:6)
        
        #############################################
        #Deletion diagnostics is another tool to examine influential observations
        print("#############################################")
        print(summary(influence.measures(ols.model)))
        
        print("#############################################")
        print("TYPE:Testing for heteroskedasticity:BP test")
        print("INTERPRETATION: if p-value less than 0.05 then heteroskedasticity exists")
        print("#############################################")
        library(lmtest)
        print(bptest(ols.model))
        
        print("#############################################")
        print("TYPE: Testing for functional misspecification; RESET TEST") 
        print("INTERPRETATION: if p-value > 0.05 then no mispecificaiton")
        print("#############################################")
        print(resettest(ols.model))
  
        print("#############################################")
        print("TYPE: Multicollinearity Test; VIF") 
        print("INTERPRETATION: if greater than 10 variable is multicollinear")      
        print("#############################################")
        print(vif(fit))
        
        print("#############################################")
        print("TYPE: Non-Linearity Test; Added Variable Plots") 
        print("INTERPRETATION: conditional regression plots for non-linearity")      
        print("#############################################")
        avPlots(fit)
        
        print("#############################################")
        print("REGRESSION MODEL") 
        print("#############################################")
        summary(fit)
}

#Calling the function
ols.diagnostics(fit)

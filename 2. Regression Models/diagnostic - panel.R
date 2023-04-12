#Based the Princeton University Panel Regression Diagnostics document
#http://www.princeton.edu/~otorres/Panel101R.pdf

#################################
#Panel Regression Diagnostic
library(plm)

data("Grunfeld", package = "AER")

#Exploring panel data
coplot(invest ~ year | firm,  type="l", data = Grunfeld)
library(car)
scatterplot(invest ~ year | firm, 
            smooth = TRUE, 
            reg.line = FALSE, 
            data = Grunfeld)

library(gplots)
plotmeans(invest ~ firm, 
          main="Heterogeineity across firms", 
          data=Grunfeld)

plotmeans(invest ~ year, 
          main="Heterogeineity across years", 
          data=Grunfeld)

###################################
#OLS Regression Model
ols <-lm(log(invest) ~ log(value) + log(capital), 
         data=Grunfeld)
summary(ols)


###################################
#Fixed Effects Model
fixed <- plm(log(invest) ~ log(value) + log(capital), 
             data=Grunfeld, 
             index=c("firm", "year"), 
             model="within")

summary(fixed)

#displaying fixed effects for each country
fixef(fixed)

#if p-value less than 0.05 then fixed effects is a better choice
pFtest(fixed, ols) 

###################################
#Random Effects Model
random <- plm(log(invest) ~ log(value) + log(capital), 
             data=Grunfeld, 
             index=c("firm", "year"), 
             model="random")

summary(random)

###################################
#deciding between fixed and random effects
#if p-value is less than 0.05 then used fixed effects
phtest(fixed, random)

###################################
#Other diagnostic tests

#Testing for time fixed effects, if p-value is less than 0.05 than use fixed effects
fixed.time <- plm(log(invest) ~ log(value) + log(capital) + factor(year), 
                  data=Grunfeld, 
                  index=c("firm","year"), model="within")
summary(fixed.time)

pFtest(fixed.time, fixed)

#Random Effects or OLS
#if p-value is less than 0.05 then use Random Effects
pool <- plm(log(invest) ~ log(value) + log(capital), 
            data=Grunfeld, index=c("firm", "year"), 
            model="pooling")
summary(pool)
plmtest(pool, type=c("bp"))


#Testing for cross section dependence
#if p is less than 0.05 then we have cross sectional independence
pcdtest(fixed, test = c("lm"))

#Testing for serial correlation
#if p is less than 0.05 than there is serial correlation
pbgtest(fixed)

#Testing for unit root/stationary
#If p-value < 0.05 then no unit roots present.
Panel.set <- plm.data(Grunfeld, index = c("firm", "year"))
library(tseries)
adf.test(Panel.set$invest, k=2)

#Testing for heteroskedasticity
#If p-value < 0.05 heteroskedasticity is present
library(lmtest)
bptest(log(invest) ~ log(value) + log(capital) + factor(firm), 
       data = Grunfeld, studentize=F)

#The --vcovHC– function estimates three heteroskedasticity-consistent covariance estimators:
        #"white1" - for general heteroskedasticity but no serial correlation. Recommended for random effects.
#"white2" - is "white1" restricted to a common variance within groups. Recommended for random effects.
#"arellano" - both heteroskedasticity and serial correlation. Recommended for fixed effects.

#The following options apply*:
        #HC0 - heteroskedasticity consistent. The default.
        #HC1,HC2, HC3 – Recommended for small samples. HC3 gives less weight to influential observations.
        #HC4 - small samples with influential observations
        #HAC - heteroskedasticity and autocorrelation consistent (type ?vcovHAC for more details)

#Heteroskedasticity for Random Effects
coeftest(random) 
coeftest(random, vcovHC) # Heteroskedasticity consistent coefficients
coeftest(random, vcovHC(random, type = "HC3")) # Heteroskedasticity consistent coefficients, type 3
t(sapply(c("HC0", "HC1", "HC2", "HC3", "HC4"), function(x) sqrt(diag(vcovHC(random, type = x)))))

#Heteroskedasticity for Random Effects
coeftest(fixed)
coeftest(fixed, vcovHC) # Heteroskedasticity consistent coefficients
coeftest(fixed, vcovHC(fixed, method = "arellano")) # Heteroskedasticity consistent coefficients (Arellano)
coeftest(fixed, vcovHC(fixed, type = "HC3")) # Heteroskedasticity consistent coefficients, type 3
t(sapply(c("HC0", "HC1", "HC2", "HC3", "HC4"), function(x) sqrt(diag(vcovHC(fixed, type = x)))))

###################
#Imports detailed company information

library(quantmod)

#Set working directory.

infiles <- setwd("C:/Users/ESPIJ090.WDW/whalewisdom - data")

stocks <- read.csv("stocks_clean.csv")

#Specifying symbols to get data for.
tickers <- as.character(stocks[,3])
ticker <-c("DIS")

#Retrieving data.

getFinancials(Symbol="DIS", src="google")
DIS <- viewFinancials(DIS.f, type=c('BS','IS','CF'), period=c('Q'))

#Transforming data into a more useful form.
DIS_t <- as.data.frame(t(DIS))
DIS_t2 <- cbind(DIS_t,ticker)

write.csv(DIS_t2,"Example_Company_Financials.csv")






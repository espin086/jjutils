###########################
#The following program cleans data the Fed macroeconomic data.

infiles <- setwd("C:/Users/ESPIJ090.WDW/whalewisdom - data/")

#Importing all files.
daily_fed <- read.csv(paste(infiles,"/DailyFed.csv",sep=""))


#Creating a date variable.
daily_fed$date <- as.Date(as.character(daily_fed$X))
daily_fed <- daily_fed[-1]


#Creating lags of these variables.
library(DataCombine)
Fed_tickers <- read.csv(paste(infiles,"/Fed_tickers.csv",sep=""))
tickers <- Fed_tickers$tickers


#BAA10Y
BAA10Y.r <- diff(log(daily_fed[,"BAA10Y"]))
BAA10Y.r.1 <- lag(BAA10Y.r)
BAA10Y.r.2 <- lag(BAA10Y.r.1)
BAA10Y.r.3 <- lag(BAA10Y.r.2)
BAA10Y.r.4 <- lag(BAA10Y.r.3)
BAA10Y.r.5 <- lag(BAA10Y.r.4)
BAA10Y.r.6 <- lag(BAA10Y.r.5)
BAA10Y.r.7 <- lag(BAA10Y.r.6)
BAA10Y.r.8 <- lag(BAA10Y.r.7)
BAA10Y.r.9 <- lag(BAA10Y.r.8)
BAA10Y.r.10 <- lag(BAA10Y.r.9)
returns<- data.frame(BAA10Y.r,BAA10Y.r.1,BAA10Y.r.2,BAA10Y.r.3,BAA10Y.r.4,BAA10Y.r.5,BAA10Y.r.6,BAA10Y.r.7,BAA10Y.r.8,BAA10Y.r.9,BAA10Y.r.10)

#DAAA
DAAA.r <- diff(log(daily_fed[,"DAAA"]))
DAAA.r.1 <- lag(DAAA.r)
DAAA.r.2 <- lag(DAAA.r.1)
DAAA.r.3 <- lag(DAAA.r.2)
DAAA.r.4 <- lag(DAAA.r.3)
DAAA.r.5 <- lag(DAAA.r.4)
DAAA.r.6 <- lag(DAAA.r.5)
DAAA.r.7 <- lag(DAAA.r.6)
DAAA.r.8 <- lag(DAAA.r.7)
DAAA.r.9 <- lag(DAAA.r.8)
DAAA.r.10 <- lag(DAAA.r.9)
returns<- data.frame(returns,DAAA.r,DAAA.r.1,DAAA.r.2,DAAA.r.3,DAAA.r.4,DAAA.r.5,DAAA.r.6,DAAA.r.7,DAAA.r.8,DAAA.r.9,DAAA.r.10)


#DCOILBRENTEU
DCOILBRENTEU.r <- diff(log(daily_fed[,"DCOILBRENTEU"]))
DCOILBRENTEU.r.1 <- lag(DCOILBRENTEU.r)
DCOILBRENTEU.r.2 <- lag(DCOILBRENTEU.r.1)
DCOILBRENTEU.r.3 <- lag(DCOILBRENTEU.r.2)
DCOILBRENTEU.r.4 <- lag(DCOILBRENTEU.r.3)
DCOILBRENTEU.r.5 <- lag(DCOILBRENTEU.r.4)
DCOILBRENTEU.r.6 <- lag(DCOILBRENTEU.r.5)
DCOILBRENTEU.r.7 <- lag(DCOILBRENTEU.r.6)
DCOILBRENTEU.r.8 <- lag(DCOILBRENTEU.r.7)
DCOILBRENTEU.r.9 <- lag(DCOILBRENTEU.r.8)
DCOILBRENTEU.r.10 <- lag(DCOILBRENTEU.r.9)
returns <- data.frame(returns,DCOILBRENTEU.r,DCOILBRENTEU.r.1,DCOILBRENTEU.r.2,DCOILBRENTEU.r.3,DCOILBRENTEU.r.4,DCOILBRENTEU.r.5,DCOILBRENTEU.r.6,DCOILBRENTEU.r.7,DCOILBRENTEU.r.8,DCOILBRENTEU.r.9,DCOILBRENTEU.r.10)


#DCOILWTICO
DCOILWTICO.r <- diff(log(daily_fed[,"DCOILWTICO"]))
DCOILWTICO.r.1 <- lag(DCOILWTICO.r)
DCOILWTICO.r.2 <- lag(DCOILWTICO.r.1)
DCOILWTICO.r.3 <- lag(DCOILWTICO.r.2)
DCOILWTICO.r.4 <- lag(DCOILWTICO.r.3)
DCOILWTICO.r.5 <- lag(DCOILWTICO.r.4)
DCOILWTICO.r.6 <- lag(DCOILWTICO.r.5)
DCOILWTICO.r.7 <- lag(DCOILWTICO.r.6)
DCOILWTICO.r.8 <- lag(DCOILWTICO.r.7)
DCOILWTICO.r.9 <- lag(DCOILWTICO.r.8)
DCOILWTICO.r.10 <- lag(DCOILWTICO.r.9)

returns <- data.frame(returns,DCOILWTICO.r,DCOILWTICO.r.1,DCOILWTICO.r.2,DCOILWTICO.r.3,DCOILWTICO.r.4,DCOILWTICO.r.5,DCOILWTICO.r.6,DCOILWTICO.r.7,DCOILWTICO.r.8,DCOILWTICO.r.9,DCOILWTICO.r.10)



#DEXCHUS
DEXCHUS.r <- diff(log(daily_fed[,"DEXCHUS"]))
DEXCHUS.r.1 <- lag(DEXCHUS.r)
DEXCHUS.r.2 <- lag(DEXCHUS.r.1)
DEXCHUS.r.3 <- lag(DEXCHUS.r.2)
DEXCHUS.r.4 <- lag(DEXCHUS.r.3)
DEXCHUS.r.5 <- lag(DEXCHUS.r.4)
DEXCHUS.r.6 <- lag(DEXCHUS.r.5)
DEXCHUS.r.7 <- lag(DEXCHUS.r.6)
DEXCHUS.r.8 <- lag(DEXCHUS.r.7)
DEXCHUS.r.9 <- lag(DEXCHUS.r.8)
DEXCHUS.r.10 <- lag(DEXCHUS.r.9)

returns <- data.frame(returns,DEXCHUS.r,DEXCHUS.r.1,DEXCHUS.r.2,DEXCHUS.r.3,DEXCHUS.r.4,DEXCHUS.r.5,DEXCHUS.r.6,DEXCHUS.r.7,DEXCHUS.r.8,DEXCHUS.r.9,DEXCHUS.r.10)




#DEXJPUS
DEXJPUS.r <- diff(log(daily_fed[,"DEXJPUS"]))
DEXJPUS.r.1 <- lag(DEXJPUS.r)
DEXJPUS.r.2 <- lag(DEXJPUS.r.1)
DEXJPUS.r.3 <- lag(DEXJPUS.r.2)
DEXJPUS.r.4 <- lag(DEXJPUS.r.3)
DEXJPUS.r.5 <- lag(DEXJPUS.r.4)
DEXJPUS.r.6 <- lag(DEXJPUS.r.5)
DEXJPUS.r.7 <- lag(DEXJPUS.r.6)
DEXJPUS.r.8 <- lag(DEXJPUS.r.7)
DEXJPUS.r.9 <- lag(DEXJPUS.r.8)
DEXJPUS.r.10 <- lag(DEXJPUS.r.9)

returns <- data.frame(returns,DEXJPUS.r,DEXJPUS.r.1,DEXJPUS.r.2,DEXJPUS.r.3,DEXJPUS.r.4,DEXJPUS.r.5,DEXJPUS.r.6,DEXJPUS.r.7,DEXJPUS.r.8,DEXJPUS.r.9,DEXJPUS.r.10)


#DEXUSEU
DEXUSEU.r <- diff(log(daily_fed[,"DEXUSEU"]))
DEXUSEU.r.1 <- lag(DEXUSEU.r)
DEXUSEU.r.2 <- lag(DEXUSEU.r.1)
DEXUSEU.r.3 <- lag(DEXUSEU.r.2)
DEXUSEU.r.4 <- lag(DEXUSEU.r.3)
DEXUSEU.r.5 <- lag(DEXUSEU.r.4)
DEXUSEU.r.6 <- lag(DEXUSEU.r.5)
DEXUSEU.r.7 <- lag(DEXUSEU.r.6)
DEXUSEU.r.8 <- lag(DEXUSEU.r.7)
DEXUSEU.r.9 <- lag(DEXUSEU.r.8)
DEXUSEU.r.10 <- lag(DEXUSEU.r.9)

returns <- data.frame(returns,DEXUSEU.r,DEXUSEU.r.1,DEXUSEU.r.2,DEXUSEU.r.3,DEXUSEU.r.4,DEXUSEU.r.5,DEXUSEU.r.6,DEXUSEU.r.7,DEXUSEU.r.8,DEXUSEU.r.9,DEXUSEU.r.10)


#DEXUSUK
DEXUSUK.r <- diff(log(daily_fed[,"DEXUSUK"]))
DEXUSUK.r.1 <- lag(DEXUSUK.r)
DEXUSUK.r.2 <- lag(DEXUSUK.r.1)
DEXUSUK.r.3 <- lag(DEXUSUK.r.2)
DEXUSUK.r.4 <- lag(DEXUSUK.r.3)
DEXUSUK.r.5 <- lag(DEXUSUK.r.4)
DEXUSUK.r.6 <- lag(DEXUSUK.r.5)
DEXUSUK.r.7 <- lag(DEXUSUK.r.6)
DEXUSUK.r.8 <- lag(DEXUSUK.r.7)
DEXUSUK.r.9 <- lag(DEXUSUK.r.8)
DEXUSUK.r.10 <- lag(DEXUSUK.r.9)

returns <- data.frame(returns,DEXUSUK.r,DEXUSUK.r.1,DEXUSUK.r.2,DEXUSUK.r.3,DEXUSUK.r.4,DEXUSUK.r.5,DEXUSUK.r.6,DEXUSUK.r.7,DEXUSUK.r.8,DEXUSUK.r.9,DEXUSUK.r.10)

#DFII10
DFII10.r <- diff(log(daily_fed[,"DFII10"]))
DFII10.r.1 <- lag(DFII10.r)
DFII10.r.2 <- lag(DFII10.r.1)
DFII10.r.3 <- lag(DFII10.r.2)
DFII10.r.4 <- lag(DFII10.r.3)
DFII10.r.5 <- lag(DFII10.r.4)
DFII10.r.6 <- lag(DFII10.r.5)
DFII10.r.7 <- lag(DFII10.r.6)
DFII10.r.8 <- lag(DFII10.r.7)
DFII10.r.9 <- lag(DFII10.r.8)
DFII10.r.10 <- lag(DFII10.r.9)

returns <- data.frame(returns,DFII10.r,DFII10.r.1,DFII10.r.2,DFII10.r.3,DFII10.r.4,DFII10.r.5,DFII10.r.6,DFII10.r.7,DFII10.r.8,DFII10.r.9,DFII10.r.10)

#DFII5
DFII5.r <- diff(log(daily_fed[,"DFII5"]))
DFII5.r.1 <- lag(DFII5.r)
DFII5.r.2 <- lag(DFII5.r.1)
DFII5.r.3 <- lag(DFII5.r.2)
DFII5.r.4 <- lag(DFII5.r.3)
DFII5.r.5 <- lag(DFII5.r.4)
DFII5.r.6 <- lag(DFII5.r.5)
DFII5.r.7 <- lag(DFII5.r.6)
DFII5.r.8 <- lag(DFII5.r.7)
DFII5.r.9 <- lag(DFII5.r.8)
DFII5.r.10 <- lag(DFII5.r.9)

returns <- data.frame(returns,DFII5.r,DFII5.r.1,DFII5.r.2,DFII5.r.3,DFII5.r.4,DFII5.r.5,DFII5.r.6,DFII5.r.7,DFII5.r.8,DFII5.r.9,DFII5.r.10)



#DGS1
DGS1.r <- diff(log(daily_fed[,"DGS1"]))
DGS1.r.1 <- lag(DGS1.r)
DGS1.r.2 <- lag(DGS1.r.1)
DGS1.r.3 <- lag(DGS1.r.2)
DGS1.r.4 <- lag(DGS1.r.3)
DGS1.r.5 <- lag(DGS1.r.4)
DGS1.r.6 <- lag(DGS1.r.5)
DGS1.r.7 <- lag(DGS1.r.6)
DGS1.r.8 <- lag(DGS1.r.7)
DGS1.r.9 <- lag(DGS1.r.8)
DGS1.r.10 <- lag(DGS1.r.9)

returns <- data.frame(returns,DGS1.r,DGS1.r.1,DGS1.r.2,DGS1.r.3,DGS1.r.4,DGS1.r.5,DGS1.r.6,DGS1.r.7,DGS1.r.8,DGS1.r.9,DGS1.r.10)

#DGS10
DGS10.r <- diff(log(daily_fed[,"DGS10"]))
DGS10.r.1 <- lag(DGS10.r)
DGS10.r.2 <- lag(DGS10.r.1)
DGS10.r.3 <- lag(DGS10.r.2)
DGS10.r.4 <- lag(DGS10.r.3)
DGS10.r.5 <- lag(DGS10.r.4)
DGS10.r.6 <- lag(DGS10.r.5)
DGS10.r.7 <- lag(DGS10.r.6)
DGS10.r.8 <- lag(DGS10.r.7)
DGS10.r.9 <- lag(DGS10.r.8)
DGS10.r.10 <- lag(DGS10.r.9)

returns <- data.frame(returns,DGS10.r,DGS10.r.1,DGS10.r.2,DGS10.r.3,DGS10.r.4,DGS10.r.5,DGS10.r.6,DGS10.r.7,DGS10.r.8,DGS10.r.9,DGS10.r.10)


#DGS2
DGS2.r <- diff(log(daily_fed[,"DGS2"]))
DGS2.r.1 <- lag(DGS2.r)
DGS2.r.2 <- lag(DGS2.r.1)
DGS2.r.3 <- lag(DGS2.r.2)
DGS2.r.4 <- lag(DGS2.r.3)
DGS2.r.5 <- lag(DGS2.r.4)
DGS2.r.6 <- lag(DGS2.r.5)
DGS2.r.7 <- lag(DGS2.r.6)
DGS2.r.8 <- lag(DGS2.r.7)
DGS2.r.9 <- lag(DGS2.r.8)
DGS2.r.10 <- lag(DGS2.r.9)

returns <- data.frame(returns,DGS2.r,DGS2.r.1,DGS2.r.2,DGS2.r.3,DGS2.r.4,DGS2.r.5,DGS2.r.6,DGS2.r.7,DGS2.r.8,DGS2.r.9,DGS2.r.10)



#DGS20
DGS20.r <- diff(log(daily_fed[,"DGS20"]))
DGS20.r.1 <- lag(DGS20.r)
DGS20.r.2 <- lag(DGS20.r.1)
DGS20.r.3 <- lag(DGS20.r.2)
DGS20.r.4 <- lag(DGS20.r.3)
DGS20.r.5 <- lag(DGS20.r.4)
DGS20.r.6 <- lag(DGS20.r.5)
DGS20.r.7 <- lag(DGS20.r.6)
DGS20.r.8 <- lag(DGS20.r.7)
DGS20.r.9 <- lag(DGS20.r.8)
DGS20.r.10 <- lag(DGS20.r.9)

returns <- data.frame(returns,DGS20.r,DGS20.r.1,DGS20.r.2,DGS20.r.3,DGS20.r.4,DGS20.r.5,DGS20.r.6,DGS20.r.7,DGS20.r.8,DGS20.r.9,DGS20.r.10)



#DGS3
DGS3.r <- diff(log(daily_fed[,"DGS3"]))
DGS3.r.1 <- lag(DGS3.r)
DGS3.r.2 <- lag(DGS3.r.1)
DGS3.r.3 <- lag(DGS3.r.2)
DGS3.r.4 <- lag(DGS3.r.3)
DGS3.r.5 <- lag(DGS3.r.4)
DGS3.r.6 <- lag(DGS3.r.5)
DGS3.r.7 <- lag(DGS3.r.6)
DGS3.r.8 <- lag(DGS3.r.7)
DGS3.r.9 <- lag(DGS3.r.8)
DGS3.r.10 <- lag(DGS3.r.9)

returns <- data.frame(returns,DGS3.r,DGS3.r.1,DGS3.r.2,DGS3.r.3,DGS3.r.4,DGS3.r.5,DGS3.r.6,DGS3.r.7,DGS3.r.8,DGS3.r.9,DGS3.r.10)


#DGS30
DGS30.r <- diff(log(daily_fed[,"DGS30"]))
DGS30.r.1 <- lag(DGS30.r)
DGS30.r.2 <- lag(DGS30.r.1)
DGS30.r.3 <- lag(DGS30.r.2)
DGS30.r.4 <- lag(DGS30.r.3)
DGS30.r.5 <- lag(DGS30.r.4)
DGS30.r.6 <- lag(DGS30.r.5)
DGS30.r.7 <- lag(DGS30.r.6)
DGS30.r.8 <- lag(DGS30.r.7)
DGS30.r.9 <- lag(DGS30.r.8)
DGS30.r.10 <- lag(DGS30.r.9)

returns <- data.frame(returns,DGS30.r,DGS30.r.1,DGS30.r.2,DGS30.r.3,DGS30.r.4,DGS30.r.5,DGS30.r.6,DGS30.r.7,DGS30.r.8,DGS30.r.9,DGS30.r.10)




#DGS3MO
DGS3MO.r <- diff(log(daily_fed[,"DGS3MO"]))
DGS3MO.r.1 <- lag(DGS3MO.r)
DGS3MO.r.2 <- lag(DGS3MO.r.1)
DGS3MO.r.3 <- lag(DGS3MO.r.2)
DGS3MO.r.4 <- lag(DGS3MO.r.3)
DGS3MO.r.5 <- lag(DGS3MO.r.4)
DGS3MO.r.6 <- lag(DGS3MO.r.5)
DGS3MO.r.7 <- lag(DGS3MO.r.6)
DGS3MO.r.8 <- lag(DGS3MO.r.7)
DGS3MO.r.9 <- lag(DGS3MO.r.8)
DGS3MO.r.10 <- lag(DGS3MO.r.9)

returns <- data.frame(returns,DGS3MO.r,DGS3MO.r.1,DGS3MO.r.2,DGS3MO.r.3,DGS3MO.r.4,DGS3MO.r.5,DGS3MO.r.6,DGS3MO.r.7,DGS3MO.r.8,DGS3MO.r.9,DGS3MO.r.10)



#DGS5
DGS5.r <- diff(log(daily_fed[,"DGS5"]))
DGS5.r.1 <- lag(DGS5.r)
DGS5.r.2 <- lag(DGS5.r.1)
DGS5.r.3 <- lag(DGS5.r.2)
DGS5.r.4 <- lag(DGS5.r.3)
DGS5.r.5 <- lag(DGS5.r.4)
DGS5.r.6 <- lag(DGS5.r.5)
DGS5.r.7 <- lag(DGS5.r.6)
DGS5.r.8 <- lag(DGS5.r.7)
DGS5.r.9 <- lag(DGS5.r.8)
DGS5.r.10 <- lag(DGS5.r.9)

returns <- data.frame(returns,DGS5.r,DGS5.r.1,DGS5.r.2,DGS5.r.3,DGS5.r.4,DGS5.r.5,DGS5.r.6,DGS5.r.7,DGS5.r.8,DGS5.r.9,DGS5.r.10)



#DGS5
DGS5.r <- diff(log(daily_fed[,"DGS5"]))
DGS5.r.1 <- lag(DGS5.r)
DGS5.r.2 <- lag(DGS5.r.1)
DGS5.r.3 <- lag(DGS5.r.2)
DGS5.r.4 <- lag(DGS5.r.3)
DGS5.r.5 <- lag(DGS5.r.4)
DGS5.r.6 <- lag(DGS5.r.5)
DGS5.r.7 <- lag(DGS5.r.6)
DGS5.r.8 <- lag(DGS5.r.7)
DGS5.r.9 <- lag(DGS5.r.8)
DGS5.r.10 <- lag(DGS5.r.9)

returns <- data.frame(returns,DGS5.r,DGS5.r.1,DGS5.r.2,DGS5.r.3,DGS5.r.4,DGS5.r.5,DGS5.r.6,DGS5.r.7,DGS5.r.8,DGS5.r.9,DGS5.r.10)


#DJIA
DJIA.r <- diff(log(daily_fed[,"DJIA"]))
DJIA.r.1 <- lag(DJIA.r)
DJIA.r.2 <- lag(DJIA.r.1)
DJIA.r.3 <- lag(DJIA.r.2)
DJIA.r.4 <- lag(DJIA.r.3)
DJIA.r.5 <- lag(DJIA.r.4)
DJIA.r.6 <- lag(DJIA.r.5)
DJIA.r.7 <- lag(DJIA.r.6)
DJIA.r.8 <- lag(DJIA.r.7)
DJIA.r.9 <- lag(DJIA.r.8)
DJIA.r.10 <- lag(DJIA.r.9)

returns <- data.frame(returns,DJIA.r,DJIA.r.1,DJIA.r.2,DJIA.r.3,DJIA.r.4,DJIA.r.5,DJIA.r.6,DJIA.r.7,DJIA.r.8,DJIA.r.9,DJIA.r.10)



#DPRIME
DPRIME.r <- diff(log(daily_fed[,"DPRIME"]))
DPRIME.r.1 <- lag(DPRIME.r)
DPRIME.r.2 <- lag(DPRIME.r.1)
DPRIME.r.3 <- lag(DPRIME.r.2)
DPRIME.r.4 <- lag(DPRIME.r.3)
DPRIME.r.5 <- lag(DPRIME.r.4)
DPRIME.r.6 <- lag(DPRIME.r.5)
DPRIME.r.7 <- lag(DPRIME.r.6)
DPRIME.r.8 <- lag(DPRIME.r.7)
DPRIME.r.9 <- lag(DPRIME.r.8)
DPRIME.r.10 <- lag(DPRIME.r.9)

returns <- data.frame(returns,DPRIME.r,DPRIME.r.1,DPRIME.r.2,DPRIME.r.3,DPRIME.r.4,DPRIME.r.5,DPRIME.r.6,DPRIME.r.7,DPRIME.r.8,DPRIME.r.9,DPRIME.r.10)


#DSWP10
DSWP10.r <- diff(log(daily_fed[,"DSWP10"]))
DSWP10.r.1 <- lag(DSWP10.r)
DSWP10.r.2 <- lag(DSWP10.r.1)
DSWP10.r.3 <- lag(DSWP10.r.2)
DSWP10.r.4 <- lag(DSWP10.r.3)
DSWP10.r.5 <- lag(DSWP10.r.4)
DSWP10.r.6 <- lag(DSWP10.r.5)
DSWP10.r.7 <- lag(DSWP10.r.6)
DSWP10.r.8 <- lag(DSWP10.r.7)
DSWP10.r.9 <- lag(DSWP10.r.8)
DSWP10.r.10 <- lag(DSWP10.r.9)

returns <- data.frame(returns,DSWP10.r,DSWP10.r.1,DSWP10.r.2,DSWP10.r.3,DSWP10.r.4,DSWP10.r.5,DSWP10.r.6,DSWP10.r.7,DSWP10.r.8,DSWP10.r.9,DSWP10.r.10)



#DTB3
DTB3.r <- diff(log(daily_fed[,"DTB3"]))
DTB3.r.1 <- lag(DTB3.r)
DTB3.r.2 <- lag(DTB3.r.1)
DTB3.r.3 <- lag(DTB3.r.2)
DTB3.r.4 <- lag(DTB3.r.3)
DTB3.r.5 <- lag(DTB3.r.4)
DTB3.r.6 <- lag(DTB3.r.5)
DTB3.r.7 <- lag(DTB3.r.6)
DTB3.r.8 <- lag(DTB3.r.7)
DTB3.r.9 <- lag(DTB3.r.8)
DTB3.r.10 <- lag(DTB3.r.9)

returns <- data.frame(returns,DTB3.r,DTB3.r.1,DTB3.r.2,DTB3.r.3,DTB3.r.4,DTB3.r.5,DTB3.r.6,DTB3.r.7,DTB3.r.8,DTB3.r.9,DTB3.r.10)


#DTWEXM
DTWEXM.r <- diff(log(daily_fed[,"DTWEXM"]))
DTWEXM.r.1 <- lag(DTWEXM.r)
DTWEXM.r.2 <- lag(DTWEXM.r.1)
DTWEXM.r.3 <- lag(DTWEXM.r.2)
DTWEXM.r.4 <- lag(DTWEXM.r.3)
DTWEXM.r.5 <- lag(DTWEXM.r.4)
DTWEXM.r.6 <- lag(DTWEXM.r.5)
DTWEXM.r.7 <- lag(DTWEXM.r.6)
DTWEXM.r.8 <- lag(DTWEXM.r.7)
DTWEXM.r.9 <- lag(DTWEXM.r.8)
DTWEXM.r.10 <- lag(DTWEXM.r.9)

returns <- data.frame(returns,DTWEXM.r,DTWEXM.r.1,DTWEXM.r.2,DTWEXM.r.3,DTWEXM.r.4,DTWEXM.r.5,DTWEXM.r.6,DTWEXM.r.7,DTWEXM.r.8,DTWEXM.r.9,DTWEXM.r.10)


#DTWEXM
DTWEXM.r <- diff(log(daily_fed[,"DTWEXM"]))
DTWEXM.r.1 <- lag(DTWEXM.r)
DTWEXM.r.2 <- lag(DTWEXM.r.1)
DTWEXM.r.3 <- lag(DTWEXM.r.2)
DTWEXM.r.4 <- lag(DTWEXM.r.3)
DTWEXM.r.5 <- lag(DTWEXM.r.4)
DTWEXM.r.6 <- lag(DTWEXM.r.5)
DTWEXM.r.7 <- lag(DTWEXM.r.6)
DTWEXM.r.8 <- lag(DTWEXM.r.7)
DTWEXM.r.9 <- lag(DTWEXM.r.8)
DTWEXM.r.10 <- lag(DTWEXM.r.9)

returns <- data.frame(returns,DTWEXM.r,DTWEXM.r.1,DTWEXM.r.2,DTWEXM.r.3,DTWEXM.r.4,DTWEXM.r.5,DTWEXM.r.6,DTWEXM.r.7,DTWEXM.r.8,DTWEXM.r.9,DTWEXM.r.10)



#DTWEXB
DTWEXB.r <- diff(log(daily_fed[,"DTWEXB"]))
DTWEXB.r.1 <- lag(DTWEXB.r)
DTWEXB.r.2 <- lag(DTWEXB.r.1)
DTWEXB.r.3 <- lag(DTWEXB.r.2)
DTWEXB.r.4 <- lag(DTWEXB.r.3)
DTWEXB.r.5 <- lag(DTWEXB.r.4)
DTWEXB.r.6 <- lag(DTWEXB.r.5)
DTWEXB.r.7 <- lag(DTWEXB.r.6)
DTWEXB.r.8 <- lag(DTWEXB.r.7)
DTWEXB.r.9 <- lag(DTWEXB.r.8)
DTWEXB.r.10 <- lag(DTWEXB.r.9)

returns <- data.frame(returns,DTWEXB.r,DTWEXB.r.1,DTWEXB.r.2,DTWEXB.r.3,DTWEXB.r.4,DTWEXB.r.5,DTWEXB.r.6,DTWEXB.r.7,DTWEXB.r.8,DTWEXB.r.9,DTWEXB.r.10)




#GBP3MTD156N
GBP3MTD156N.r <- diff(log(daily_fed[,"GBP3MTD156N"]))
GBP3MTD156N.r.1 <- lag(GBP3MTD156N.r)
GBP3MTD156N.r.2 <- lag(GBP3MTD156N.r.1)
GBP3MTD156N.r.3 <- lag(GBP3MTD156N.r.2)
GBP3MTD156N.r.4 <- lag(GBP3MTD156N.r.3)
GBP3MTD156N.r.5 <- lag(GBP3MTD156N.r.4)
GBP3MTD156N.r.6 <- lag(GBP3MTD156N.r.5)
GBP3MTD156N.r.7 <- lag(GBP3MTD156N.r.6)
GBP3MTD156N.r.8 <- lag(GBP3MTD156N.r.7)
GBP3MTD156N.r.9 <- lag(GBP3MTD156N.r.8)
GBP3MTD156N.r.10 <- lag(GBP3MTD156N.r.9)

returns <- data.frame(returns,GBP3MTD156N.r,GBP3MTD156N.r.1,GBP3MTD156N.r.2,GBP3MTD156N.r.3,GBP3MTD156N.r.4,GBP3MTD156N.r.5,GBP3MTD156N.r.6,GBP3MTD156N.r.7,GBP3MTD156N.r.8,GBP3MTD156N.r.9,GBP3MTD156N.r.10)



#GOLDAMGBD228NLBM
GOLDAMGBD228NLBM.r <- diff(log(daily_fed[,"GOLDAMGBD228NLBM"]))
GOLDAMGBD228NLBM.r.1 <- lag(GOLDAMGBD228NLBM.r)
GOLDAMGBD228NLBM.r.2 <- lag(GOLDAMGBD228NLBM.r.1)
GOLDAMGBD228NLBM.r.3 <- lag(GOLDAMGBD228NLBM.r.2)
GOLDAMGBD228NLBM.r.4 <- lag(GOLDAMGBD228NLBM.r.3)
GOLDAMGBD228NLBM.r.5 <- lag(GOLDAMGBD228NLBM.r.4)
GOLDAMGBD228NLBM.r.6 <- lag(GOLDAMGBD228NLBM.r.5)
GOLDAMGBD228NLBM.r.7 <- lag(GOLDAMGBD228NLBM.r.6)
GOLDAMGBD228NLBM.r.8 <- lag(GOLDAMGBD228NLBM.r.7)
GOLDAMGBD228NLBM.r.9 <- lag(GOLDAMGBD228NLBM.r.8)
GOLDAMGBD228NLBM.r.10 <- lag(GOLDAMGBD228NLBM.r.9)

returns <- data.frame(returns,GOLDAMGBD228NLBM.r,GOLDAMGBD228NLBM.r.1,GOLDAMGBD228NLBM.r.2,GOLDAMGBD228NLBM.r.3,GOLDAMGBD228NLBM.r.4,GOLDAMGBD228NLBM.r.5,GOLDAMGBD228NLBM.r.6,GOLDAMGBD228NLBM.r.7,GOLDAMGBD228NLBM.r.8,GOLDAMGBD228NLBM.r.9,GOLDAMGBD228NLBM.r.10)




#SP500
SP500.r <- diff(log(daily_fed[,"SP500"]))
SP500.r.1 <- lag(SP500.r)
SP500.r.2 <- lag(SP500.r.1)
SP500.r.3 <- lag(SP500.r.2)
SP500.r.4 <- lag(SP500.r.3)
SP500.r.5 <- lag(SP500.r.4)
SP500.r.6 <- lag(SP500.r.5)
SP500.r.7 <- lag(SP500.r.6)
SP500.r.8 <- lag(SP500.r.7)
SP500.r.9 <- lag(SP500.r.8)
SP500.r.10 <- lag(SP500.r.9)

returns <- data.frame(returns,SP500.r,SP500.r.1,SP500.r.2,SP500.r.3,SP500.r.4,SP500.r.5,SP500.r.6,SP500.r.7,SP500.r.8,SP500.r.9,SP500.r.10)


#T10Y2Y
T10Y2Y.r <- diff(log(daily_fed[,"T10Y2Y"]))
T10Y2Y.r.1 <- lag(T10Y2Y.r)
T10Y2Y.r.2 <- lag(T10Y2Y.r.1)
T10Y2Y.r.3 <- lag(T10Y2Y.r.2)
T10Y2Y.r.4 <- lag(T10Y2Y.r.3)
T10Y2Y.r.5 <- lag(T10Y2Y.r.4)
T10Y2Y.r.6 <- lag(T10Y2Y.r.5)
T10Y2Y.r.7 <- lag(T10Y2Y.r.6)
T10Y2Y.r.8 <- lag(T10Y2Y.r.7)
T10Y2Y.r.9 <- lag(T10Y2Y.r.8)
T10Y2Y.r.10 <- lag(T10Y2Y.r.9)

returns <- data.frame(returns,T10Y2Y.r,T10Y2Y.r.1,T10Y2Y.r.2,T10Y2Y.r.3,T10Y2Y.r.4,T10Y2Y.r.5,T10Y2Y.r.6,T10Y2Y.r.7,T10Y2Y.r.8,T10Y2Y.r.9,T10Y2Y.r.10)


#T10YIE
T10YIE.r <- diff(log(daily_fed[,"T10YIE"]))
T10YIE.r.1 <- lag(T10YIE.r)
T10YIE.r.2 <- lag(T10YIE.r.1)
T10YIE.r.3 <- lag(T10YIE.r.2)
T10YIE.r.4 <- lag(T10YIE.r.3)
T10YIE.r.5 <- lag(T10YIE.r.4)
T10YIE.r.6 <- lag(T10YIE.r.5)
T10YIE.r.7 <- lag(T10YIE.r.6)
T10YIE.r.8 <- lag(T10YIE.r.7)
T10YIE.r.9 <- lag(T10YIE.r.8)
T10YIE.r.10 <- lag(T10YIE.r.9)

returns <- data.frame(returns,T10YIE.r,T10YIE.r.1,T10YIE.r.2,T10YIE.r.3,T10YIE.r.4,T10YIE.r.5,T10YIE.r.6,T10YIE.r.7,T10YIE.r.8,T10YIE.r.9,T10YIE.r.10)



#T5YIE
T5YIE.r <- diff(log(daily_fed[,"T5YIE"]))
T5YIE.r.1 <- lag(T5YIE.r)
T5YIE.r.2 <- lag(T5YIE.r.1)
T5YIE.r.3 <- lag(T5YIE.r.2)
T5YIE.r.4 <- lag(T5YIE.r.3)
T5YIE.r.5 <- lag(T5YIE.r.4)
T5YIE.r.6 <- lag(T5YIE.r.5)
T5YIE.r.7 <- lag(T5YIE.r.6)
T5YIE.r.8 <- lag(T5YIE.r.7)
T5YIE.r.9 <- lag(T5YIE.r.8)
T5YIE.r.10 <- lag(T5YIE.r.9)

returns <- data.frame(returns,T5YIE.r,T5YIE.r.1,T5YIE.r.2,T5YIE.r.3,T5YIE.r.4,T5YIE.r.5,T5YIE.r.6,T5YIE.r.7,T5YIE.r.8,T5YIE.r.9,T5YIE.r.10)




#T5YIFR
T5YIFR.r <- diff(log(daily_fed[,"T5YIFR"]))
T5YIFR.r.1 <- lag(T5YIFR.r)
T5YIFR.r.2 <- lag(T5YIFR.r.1)
T5YIFR.r.3 <- lag(T5YIFR.r.2)
T5YIFR.r.4 <- lag(T5YIFR.r.3)
T5YIFR.r.5 <- lag(T5YIFR.r.4)
T5YIFR.r.6 <- lag(T5YIFR.r.5)
T5YIFR.r.7 <- lag(T5YIFR.r.6)
T5YIFR.r.8 <- lag(T5YIFR.r.7)
T5YIFR.r.9 <- lag(T5YIFR.r.8)
T5YIFR.r.10 <- lag(T5YIFR.r.9)

returns <- data.frame(returns,T5YIFR.r,T5YIFR.r.1,T5YIFR.r.2,T5YIFR.r.3,T5YIFR.r.4,T5YIFR.r.5,T5YIFR.r.6,T5YIFR.r.7,T5YIFR.r.8,T5YIFR.r.9,T5YIFR.r.10)



#TEDRATE
TEDRATE.r <- diff(log(daily_fed[,"TEDRATE"]))
TEDRATE.r.1 <- lag(TEDRATE.r)
TEDRATE.r.2 <- lag(TEDRATE.r.1)
TEDRATE.r.3 <- lag(TEDRATE.r.2)
TEDRATE.r.4 <- lag(TEDRATE.r.3)
TEDRATE.r.5 <- lag(TEDRATE.r.4)
TEDRATE.r.6 <- lag(TEDRATE.r.5)
TEDRATE.r.7 <- lag(TEDRATE.r.6)
TEDRATE.r.8 <- lag(TEDRATE.r.7)
TEDRATE.r.9 <- lag(TEDRATE.r.8)
TEDRATE.r.10 <- lag(TEDRATE.r.9)

returns <- data.frame(returns,TEDRATE.r,TEDRATE.r.1,TEDRATE.r.2,TEDRATE.r.3,TEDRATE.r.4,TEDRATE.r.5,TEDRATE.r.6,TEDRATE.r.7,TEDRATE.r.8,TEDRATE.r.9,TEDRATE.r.10)


#USD12MD156N
USD12MD156N.r <- diff(log(daily_fed[,"USD12MD156N"]))
USD12MD156N.r.1 <- lag(USD12MD156N.r)
USD12MD156N.r.2 <- lag(USD12MD156N.r.1)
USD12MD156N.r.3 <- lag(USD12MD156N.r.2)
USD12MD156N.r.4 <- lag(USD12MD156N.r.3)
USD12MD156N.r.5 <- lag(USD12MD156N.r.4)
USD12MD156N.r.6 <- lag(USD12MD156N.r.5)
USD12MD156N.r.7 <- lag(USD12MD156N.r.6)
USD12MD156N.r.8 <- lag(USD12MD156N.r.7)
USD12MD156N.r.9 <- lag(USD12MD156N.r.8)
USD12MD156N.r.10 <- lag(USD12MD156N.r.9)

returns <- data.frame(returns,USD12MD156N.r,USD12MD156N.r.1,USD12MD156N.r.2,USD12MD156N.r.3,USD12MD156N.r.4,USD12MD156N.r.5,USD12MD156N.r.6,USD12MD156N.r.7,USD12MD156N.r.8,USD12MD156N.r.9,USD12MD156N.r.10)




#USD3MTD156N
USD3MTD156N.r <- diff(log(daily_fed[,"USD3MTD156N"]))
USD3MTD156N.r.1 <- lag(USD3MTD156N.r)
USD3MTD156N.r.2 <- lag(USD3MTD156N.r.1)
USD3MTD156N.r.3 <- lag(USD3MTD156N.r.2)
USD3MTD156N.r.4 <- lag(USD3MTD156N.r.3)
USD3MTD156N.r.5 <- lag(USD3MTD156N.r.4)
USD3MTD156N.r.6 <- lag(USD3MTD156N.r.5)
USD3MTD156N.r.7 <- lag(USD3MTD156N.r.6)
USD3MTD156N.r.8 <- lag(USD3MTD156N.r.7)
USD3MTD156N.r.9 <- lag(USD3MTD156N.r.8)
USD3MTD156N.r.10 <- lag(USD3MTD156N.r.9)

returns <- data.frame(returns,USD3MTD156N.r,USD3MTD156N.r.1,USD3MTD156N.r.2,USD3MTD156N.r.3,USD3MTD156N.r.4,USD3MTD156N.r.5,USD3MTD156N.r.6,USD3MTD156N.r.7,USD3MTD156N.r.8,USD3MTD156N.r.9,USD3MTD156N.r.10)


#USD6MTD156N
USD6MTD156N.r <- diff(log(daily_fed[,"USD6MTD156N"]))
USD6MTD156N.r.1 <- lag(USD6MTD156N.r)
USD6MTD156N.r.2 <- lag(USD6MTD156N.r.1)
USD6MTD156N.r.3 <- lag(USD6MTD156N.r.2)
USD6MTD156N.r.4 <- lag(USD6MTD156N.r.3)
USD6MTD156N.r.5 <- lag(USD6MTD156N.r.4)
USD6MTD156N.r.6 <- lag(USD6MTD156N.r.5)
USD6MTD156N.r.7 <- lag(USD6MTD156N.r.6)
USD6MTD156N.r.8 <- lag(USD6MTD156N.r.7)
USD6MTD156N.r.9 <- lag(USD6MTD156N.r.8)
USD6MTD156N.r.10 <- lag(USD6MTD156N.r.9)

returns <- data.frame(returns,USD6MTD156N.r,USD6MTD156N.r.1,USD6MTD156N.r.2,USD6MTD156N.r.3,USD6MTD156N.r.4,USD6MTD156N.r.5,USD6MTD156N.r.6,USD6MTD156N.r.7,USD6MTD156N.r.8,USD6MTD156N.r.9,USD6MTD156N.r.10)



####################################
#Getting dates.
daily_fed2 <-daily_fed[2:nrow(daily_fed),]


returns <- data.frame(daily_fed2$date,returns)
library(reshape)
returns <- rename(returns, c(daily_fed2.date="date"))

returns <- na.omit(returns)

#Exporting clean data set.
write.csv(returns,paste(infiles,"/DailyFed_clean.csv",sep=""))



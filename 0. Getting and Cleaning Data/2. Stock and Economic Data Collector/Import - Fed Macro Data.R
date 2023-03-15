#The following program downloads data from the U.S. Federal Reserve Bank
library(quantmod)

fed_tickers <- read.csv("C:/Users/ESPIJ090.WDW/whalewisdom - data/Fed_tickers.csv")
tickers <-as.character(fed_tickers[,1])

getSymbols(tickers,src="FRED")


z <- merge(BAA10Y,DAAA)
z <- merge(z,DCOILBRENTEU)
z <- merge(z,DCOILWTICO)
z <- merge(z,DEXCHUS)
z <- merge(z,DEXJPUS)
z <- merge(z,DEXUSUK)
z <- merge(z,DGS1)
z <- merge(z,DGS10)
z <- merge(z,DGS2)
z <- merge(z,DGS3)
z <- merge(z,DGS30)
z <- merge(z,DGS3MO)
z <- merge(z,DGS5)
z <- merge(z,DPRIME)
z <- merge(z,DTB3)
z <- merge(z,DTWEXM)
z <- merge(z,GBP3MTD156N)
z <- merge(z,GOLDAMGBD228NLBM)
z <- merge(z,T10Y2Y)
z <- merge(z,TEDRATE)
z <- merge(z,USD12MD156N)
z <- merge(z,USD1MTD156N)
z <- merge(z,USD3MTD156N)
z <- merge(z,USD6MTD156N)


z <- as.data.frame(z)

z <- na.omit(z)


write.csv(z,"C:/Users/ESPIJ090.WDW/whalewisdom - data/DailyFed.csv", row.names = TRUE)








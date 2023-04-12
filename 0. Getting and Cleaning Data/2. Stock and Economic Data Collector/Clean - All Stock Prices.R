#####################################
#The following program cleans and prepares the data for All Stock Prices.

infiles <- setwd("C:/Users/ESPIJ090.WDW/whalewisdom - data/")


#Importing all files.
AllStockPrices <- read.csv(paste(infiles,"/AllStockPrices.csv",sep=""))

#Deleting columns (stocks) that only have NA values.
AllStockPrices<-AllStockPrices[,colSums(is.na(AllStockPrices)) != nrow(AllStockPrices)]

#Creating a date variable.
AllStockPrices$date <- as.Date(as.character(AllStockPrices$X.1))

AllStockPrices <- AllStockPrices[-1]

#Melting and reshaping so data is tidy.
library(reshape)
AllStockPrices <- melt(AllStockPrices, id=c("date"))
names(AllStockPrices) <- c("date","ticker","stock_price")

#stocks_clean <- AllStockPrices[ which(AllStockPrices$ticker=='MMM' | AllStockPrices$ticker=='AXP'|AllStockPrices$ticker=='T' |AllStockPrices$ticker=='BA'|AllStockPrices$ticker=='CAT'|AllStockPrices$ticker=='CVX'|AllStockPrices$ticker=='CSCO'|AllStockPrices$ticker=='KO'|AllStockPrices$ticker=='DIS'|AllStockPrices$ticker=='DD'|AllStockPrices$ticker=='XOM'|AllStockPrices$ticker=='GE'|AllStockPrices$ticker=='GS'|AllStockPrices$ticker=='HD'|AllStockPrices$ticker=='IBM'|AllStockPrices$ticker=='INTC'|AllStockPrices$ticker=='JNJ'|AllStockPrices$ticker=='JPM'|AllStockPrices$ticker=='MCD'|AllStockPrices$ticker=='MRK'|AllStockPrices$ticker=='MSFT'|AllStockPrices$ticker=='NIKE'|AllStockPrices$ticker=='PFE'|AllStockPrices$ticker=='PG'|AllStockPrices$ticker=='TRV'|AllStockPrices$ticker=='UTX'|AllStockPrices$ticker=='UNH'|AllStockPrices$ticker=='VZ'|AllStockPrices$ticker=='WMT'), ]

#Keep Specific Stock
#stocks_clean <- AllStockPrices[ which(AllStockPrices$ticker=='DIS'), ]

#All Stocks
stocks_clean <- AllStockPrices

#Function that lags key variables worth examining
library(DataCombine)

slide.fun <- function(df = stocks_clean, variable = "stock_price" , groupby = "ticker", start = -1, end = -10){
        for (i in start:end){
                df <- slide(df, Var = variable, GroupVar = groupby ,slideBy = i)
        }
}

#Lagging stock price
slide.fun(variable = "stock_price")


#Computing returns
stocks_clean$returns <- log(stocks_clean[,3]) - log(stocks_clean[,4])

#Lagging returns
slide.fun(variable = "returns")


#Keeping only daily returns
myvars <- c("date", "ticker","returns","returns-1","returns-2","returns-3","returns-4","returns-5","returns-6","returns-7","returns-8","returns-9","returns-10")
stocks_clean <- stocks_clean[myvars]


#Exporting clean data set.
write.csv(stocks_clean,paste(infiles,"/AllStockPrices_clean.csv",sep=""))


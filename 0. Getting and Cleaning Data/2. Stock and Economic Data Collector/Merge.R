#####################################
#The following program merges data sources into a flat table.

infiles <- setwd("C:/Users/ESPIJ090.WDW/whalewisdom - data/")


#Importing all files and filtering observations and columns.
stocks_clean <- read.csv(paste(infiles,"/AllStockPrices_clean.csv",sep=""))
drops <- c("X")
stocks_clean<-stocks_clean[,!(names(stocks_clean) %in% drops)]


fed_clean <- read.csv(paste(infiles,"/DailyFed_clean.csv",sep=""))
drops <- c("X")
fed_clean<-fed_clean[,!(names(fed_clean) %in% drops)]


#Exporting merged file
merged <- merge(x=stocks_clean, y=fed_clean,by.date = "date",by.date="date",all.x= TRUE)

#removing missing variables and sorting
merged <- merged[order(merged$ticker, merged$date),]

#Creating test and validation dates.
library(lubridate)
merged$date <- as.Date(merged$date)
merged$month <- month(merged$date)
merged$year <- year(merged$date)


#Removing missing observations - greatly limits data to only the most recent fed variable
merged <- na.omit(merged)

#Categorizing Returns.
library(Hmisc)
merged$returns<-cut2(merged$returns, g=5)


#Removing Near Zero Variance variables.
nzv <- nearZeroVar(merged, saveMetrics= TRUE)
nzv<-nzv[nzv$nzv=="TRUE",]
nzv<-row.names(nzv)
myvars <- names(merged) %in% nzv
merged <- merged[!myvars]

#Creating training and test datasets.
training <- merged[ which(merged$year < 2010), ]
testing <- merged[ which(merged$year >= 2010 & merged$year < 2014)  , ]
validation <- merged[ which(merged$year >= 2015), ]


#Removing date and month variables for consistency.
myvars <- names(training) %in% c("date", "month","year","stock_price")
training <- training[!myvars]
testing <- testing[!myvars]
validation <- validation[!myvars]


#Exporting dataset for analysis in Rattle.
write.csv(training,"training.csv")
write.csv(testing,"testing.csv")
write.csv(validation,"validation.csv")














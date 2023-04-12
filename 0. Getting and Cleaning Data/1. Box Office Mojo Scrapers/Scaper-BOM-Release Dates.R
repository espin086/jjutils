######################################
#Collecting film meta-data - Box Office Mojo
library(XML)       #Used to scrape film data
library(lubridate) #Used to format release dates
library(rattle)    #Used to produce summary statistics after data collection and cleaning

#Source of Data: http://www.boxofficemojo.com/schedule/?view=distributor&p=.htm

#List of distributors, you can add additional lists by clicking on the link above
dist <- as.list(c("buenavista", "fox", "paramount", "sony","universal", "warnerbros"))
#Empty container to hold data per distributor
dist.data <- list()

#Web Scraping Function
scrape.data <- function(x){
        #produces a URL to pass to an XML libray function based on distributor
        urls <- paste0("http://www.boxofficemojo.com/schedule/?view=distributor&id=", x ,".htm")
        #Extrcting relevant table from the web
        input <- readHTMLTable(urls)[[1]]
        #The first few rows contain irrelevant header info, so they are deleted
        input.clean <- input[-c(1,2,3,4),]
        #Creates new variable to identify the distributor in the dataset
        input.clean$dist <- c(x)
        #Remaing the varibles in the dataframe
        names(input.clean) <- c("Movie", "Release.Date", "Distributor")
        #Removing non-standard or missing dates (is the standard xx/xx/xx)
        clean.data <- input.clean[complete.cases(input.clean),]
        clean.data <- clean.data[ which(clean.data$Release.Date != "TBD"), ]
        clean.data <- clean.data[ which(clean.data$Release.Date != "2016"), ]
        clean.data <- clean.data[ which(clean.data$Release.Date != "2017"), ]
        clean.data <- clean.data[ which(clean.data$Release.Date != "2018"), ]
        #Saving results in a list, so an family of apply functions can loop through a list of dist
        
        clean.data$Release.Date <- as.Date(clean.data$Release.Date, "%m/%d/%y")
        
        #Extracting Useful Date Info
        clean.data$Release.Date.Year <- year(clean.data$Release.Date)
        clean.data$Release.Date.Month <- month(clean.data$Release.Date)
        clean.data$Release.Week.Year <- week(clean.data$Release.Date)
        clean.data$Release.Date.Weekday <- wday(clean.data$Release.Date, label = TRUE)
        
        
        
        dist.data[[x]] <- clean.data
        #The function output is this list
        dist.data
}

#Applying scraping function to distributor list using sapply fucntion
release.list <- sapply(dist, scrape.data)

#Stacking Data
release.df <- do.call("rbind", release.list)

#Exporting Data for Further Analysis
setwd("~/Documents/HollywoodModels/0. Data/2. Clean Data")
write.csv(release.df, "Future Film Release Dates.csv")

#Opening up Rattle to Explore Further
rattle()


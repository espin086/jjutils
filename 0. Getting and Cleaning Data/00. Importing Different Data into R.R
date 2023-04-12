
###############################################################
#Downloading CSV File from the Internet and importin it to R
setwd("C:/Users/ESPIJ090.WDW/datasciencecoursera - data/")
#Creates a folder for data if there isn't one already.
if (!file.exists("data")) {
        dir.create("data")
}

fileUrl <- "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
download.file(fileUrl, destfile = "./data/cameras.csv")
dateDownloaded <- date()

cameraData <- read.csv("./data/cameras.csv")


###############################################################
#Downloading XLS File from the Internet and importin it to R
if(!file.exists("data")){dir.create("data")}
fileUrl <- "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.xlsx?accessType=DOWNLOAD"
download.file(fileUrl,destfile="./data/cameras.xlsx")
dateDownloaded <- date()

library(xlsx)
cameraData <- read.xlsx("./data/cameras.xlsx",sheetIndex=1,header=TRUE)
head(cameraData)

###############################################################
#Downloading XML and importin it to R

library(XML)
fileUrl <- "http://www.w3schools.com/xml/simple.xml"
doc <- xmlTreeParse(fileUrl,useInternal=TRUE)
rootNode <- xmlRoot(doc)
xmlName(rootNode)

#Exploring XLM
names(rootNode)
rootNode[[1]]
rootNode[[1]][[1]]

#Extracting menu items and prices.
xpathSApply(rootNode,"//name",xmlValue)
xpathSApply(rootNode,"//price",xmlValue)
xpathSApply(rootNode,"//calories",xmlValue)

#Programmatically extra XML data
xmlSApply(rootNode,xmlValue)

#Extracting menu items and prices.
xpathSApply(rootNode,"//name",xmlValue)
xpathSApply(rootNode,"//price",xmlValue)
xpathSApply(rootNode,"//calories",xmlValue)

#ESPN Example


fileUrl <- "http://espn.go.com/nfl/team/_/name/bal/baltimore-ravens"
doc <- htmlTreeParse(fileUrl,useInternal=TRUE)

scores <- xpathSApply(doc,"//li[@class='score']",xmlValue)
teams <- xpathSApply(doc,"//li[@class='team-name']",xmlValue)
status <- xpathSApply(doc,"//li[@class='game-status']",xmlValue)

scores
teams
status

###############################################################
#Downloading JSON Files
library(jsonlite)
jsonData <- fromJSON("https://api.github.com/users/jtleek/repos")
names(jsonData)

#Exploring the JSON file
jsonData$name
names(jsonData$owner)
jsonData$owner$login

#Writing data frames to JSON
myjson <- toJSON(iris, pretty=TRUE)
cat(myjson)

#Writing from JSON to data frame
iris2 <- fromJSON(myjson)
head(iris2)

###############################################################
#Data Table Operations

library(data.table)
DT = data.table(x=rnorm(9),y=rep(c("a","b","c"),each=3),z=rnorm(9))
head(DT,3)

#Subseting Rows
DT[2,]
DT[c(2,3)]
DT[DT$y=="a",]

#Summarizing Variables
DT[,list(mean(x),sum(z),sum(x))]
DT[,table(y)]


#Adding new columns
DT[,w:=z^2]
DT2 <- DT
DT[, y:= 2]

DT[,a:=x>0]
DT[,b:= mean(x+w),by=a]


#Counting the elements of a factor variable, built in special variable
set.seed(123);
DT <- data.table(x=sample(letters[1:3], 1E5, TRUE))
DT[, .N, by=x]

#Creating keys for subsetting
DT <- data.table(x=rep(c("a","b","c"),each=100), y=rnorm(300))
setkey(DT, x)
DT['a']

#Creating keys for subsetting.
DT1 <- data.table(x=c('a', 'a', 'b', 'dt1'), y=1:4)
DT2 <- data.table(x=c('a', 'b', 'dt2'), z=5:7)
setkey(DT1, x); setkey(DT2, x)
merge(DT1, DT2)

#Fast reading of large files.
big_df <- data.frame(x=rnorm(1E6), y=rnorm(1E6))
file <- tempfile()

write.table(big_df, file=file, row.names=FALSE, col.names=TRUE, sep="\t", quote=FALSE)
system.time(fread(file))


####################
#MySQL
library(RMySQL)

#Show number of databases.
ucscDb <- dbConnect(MySQL(),user="genome",host="genome-mysql.cse.ucsc.edu")
result <- dbGetQuery(ucscDb,"show databases;")
dbDisconnect(ucscDb)

#Show tables in a particular database.
hg19 <- dbConnect(MySQL(),user="genome", db="hg19",host="genome-mysql.cse.ucsc.edu")
allTables <- dbListTables(hg19)
length(allTables)
allTables[1:5]

#Get the dimensions of a particular table.
dbListFields(hg19,"affyU133Plus2")#Counts variables.
dbGetQuery(hg19, "select count(*) from affyU133Plus2")#Counts observations.

#Read a table into R.
affyData <- dbReadTable(hg19, "affyU133Plus2")
head(affyData)

#Select only a specific subset.
#selecting based on values in a variable.
query <- dbSendQuery(hg19, "select * from affyU133Plus2 where misMatches between 1 and 3")
affyMis <- fetch(query)
quantile(affyMis$misMatches)

#Selecting only the top 10 observations.
affyMisSmall <- fetch(query,n=10); dbClearResult(query);

#Again, must close the connection.
dbDisconnect(hg19)

####################
#HDF5

source("http://bioconductor.org/biocLite.R")
biocLite("rhdf5")

#Creates interface with hdf5 databases
library(rhdf5)
created = h5createFile("example.h5")
created

#Create Groups
created = h5createGroup("example.h5","foo")
created = h5createGroup("example.h5","baa")
created = h5createGroup("example.h5","foo/foobaa")
h5ls("example.h5")

#Write data to groups
A = matrix(1:10,nr=5,nc=2)
h5write(A, "example.h5","foo/A")
B = array(seq(0.1,2.0,by=0.1),dim=c(5,2,2))
attr(B, "scale") <- "liter"
h5write(B, "example.h5","foo/foobaa/B")
h5ls("example.h5")

#Write a dataset.
df = data.frame(1L:5L,seq(0,1,length.out=5),
                c("ab","cde","fghi","a","s"), stringsAsFactors=FALSE)
h5write(df, "example.h5","df")
h5ls("example.h5")

#Reading data
readA = h5read("example.h5","foo/A")
readB = h5read("example.h5","foo/foobaa/B")
readdf= h5read("example.h5","df")
readA

#Writing and reading chunks.
h5write(c(12,13,14),"example.h5","foo/A",index=list(1:3,1))
h5read("example.h5","foo/A")


####################
#Web Data

#Reading HTML Code
con = url("http://scholar.google.com/citations?user=HI-I6C0AAAAJ&hl=en")
htmlCode = readLines(con)
close(con)
htmlCode

#Parsing HTML with XML package.
library(XML)
url <- "http://scholar.google.com/citations?user=HI-I6C0AAAAJ&hl=en"
html <- htmlTreeParse(url, useInternalNodes=T)

xpathSApply(html, "//title", xmlValue)

xpathSApply(html, "//td[@id='col-citedby']", xmlValue)

#Same Example as above but with httr package.
library(httr); html2 = GET(url)
content2 = content(html2,as="text")
parsedHtml = htmlParse(content2,asText=TRUE)
xpathSApply(parsedHtml, "//title", xmlValue)

#Accessing webistes with passwords - try this with jacksons SQL database!
pg2 = GET("http://httpbin.org/basic-auth/user/passwd",authenticate("user","passwd"))
pg2

names(pg2)

#Using Handles
google = handle("http://google.com")
pg1 = GET(handle=google,path="/")
pg2 = GET(handle=google,path="search")


####################
#APIs

#Getting data form Twitter
myapp = oauth_app("twitter",
                  key="yourConsumerKeyHere",secret="yourConsumerSecretHere")
sig = sign_oauth1.0(myapp,
                    token = "yourTokenHere",
                    token_secret = "yourTokenSecretHere")
homeTL = GET("https://api.twitter.com/1.1/statuses/home_timeline.json", sig)

#Converting to JSON
json1 = content(homeTL)
json2 = jsonlite::fromJSON(toJSON(json1))
json2[1,1:4]




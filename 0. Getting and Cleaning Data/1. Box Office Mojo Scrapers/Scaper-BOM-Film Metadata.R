######################################
#Collecting film meta-data - Box Office Mojo


library(XML) #Used to parse out film data

u <- "http://www.boxofficemojo.com/movies/?id=2guns.htm"

#Contains a host of data
test.1 <- readHTMLTable(u)[[1]]

#Contains a host of data
#test.2 <- readHTMLTable(u)[[2]]#Empty

#Contains a host of data
test.3 <- readHTMLTable(u)[[3]]

#Contains a small table with key data
test.4 <- readHTMLTable(u)[[4]]


#Contains a small table with key data
test.5 <- readHTMLTable(u)[[5]]

#Contains a small table with key data
test.6 <- readHTMLTable(u)[[6]]

#Contains a large table with key data
test.7 <- readHTMLTable(u)[[7]]

#Contains a large table with key data
test.8 <- readHTMLTable(u)[[8]]

#Contains a large table with key data
test.9 <- readHTMLTable(u)[[9]]

#Contains a large table with key data
test.10 <- readHTMLTable(u)[[10]]

#Contains a large table with key data
test.11 <- readHTMLTable(u)[[11]]

#Contains a large table with key data
#test.12 <- readHTMLTable(u)[[12]]#Empty

#Contains a large table with key data
#test.13 <- readHTMLTable(u)[[13]]#Empty

#Contains a large table with key data
#test.14 <- readHTMLTable(u)[[14]]#Empty

#Table that contains the talent in the film
test.15 <- readHTMLTable(u)[[15]]

#Ranking of the film
test.16 <- readHTMLTable(u)[[16]]

#Further ranking of film
test.17 <- readHTMLTable(u)[[17]]

#Further ranking of film
test.18 <- readHTMLTable(u)[[18]]



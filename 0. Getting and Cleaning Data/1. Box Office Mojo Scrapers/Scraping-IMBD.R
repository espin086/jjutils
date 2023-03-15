
library(dplyr)
library(pbapply)
library(omdbapi)

#Reading in data with list of movies to examine
setwd("~/Desktop")

title.key <- read.csv("titlekey.csv", stringsAsFactors = FALSE)
title.key <- title.key[which(title.key$imdbid != ""),]
imdbid <- as.vector(title.key$imdbid)

#Feeding IMBD ID Numbers into function that will find movie info
title.info <- lapply(imdbid, find_by_id)
df <- data.frame(matrix(unlist(title.info), nrow = length(title.info), byrow=T))

#Renaming the columns with the appropriate titles from title.info list
names(df) <- c( "Title",
"Year",
"Rated",
"Released",
"Runtime",
"Genre",
"Director",
"Writer",
"Actors",
"Plot",
"Language",
"Country",
"Awards",
"Poster",
"Metascore",
"imdbRating",
"imdbVotes",
"imdbID",
"Type")

write.csv(df, "IMBD Rating - OMBD API.csv")

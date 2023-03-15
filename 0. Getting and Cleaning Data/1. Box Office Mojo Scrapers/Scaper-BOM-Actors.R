library(XML)

# Step 1: construct URLs
urls <- paste("http://www.boxofficemojo.com/people/?view=Actor&pagenum=", 1:3, "&sort=person&order=ASC&p=.htm", sep = "")

# Step 2: scrape website
get_table <- function(u) {
        table <- readHTMLTable(u)[[3]]
        names(table) <- c("Actor", "Total.Gross", "Num.Movies", "Avg.Per.Movie", "No.1 Movie", "Gross.of.No.1.Movie")
        df <- as.data.frame(lapply(table[-1, ], as.character), stringsAsFactors=FALSE)
        df <- as.data.frame(df, stringsAsFactors=FALSE)
        return(df)
}

df <- do.call("rbind", lapply(urls, get_table))


# Step 3: clean dataframe
clean_df <- function(df) {
        clean <- function(col) {
                col <- gsub("$", "", col, fixed = TRUE)
                col <- gsub("%", "", col, fixed = TRUE)
                col <- gsub(",", "", col, fixed = TRUE)
                col <- gsub("^", "", col, fixed = TRUE)
                return(col)
        }
        
        df <- sapply(df, clean)
        df <- as.data.frame(df, stringsAsFactors=FALSE)
        return(df)
}
df <- clean_df(df)        


# Step 4: set column types
s <- c(2:4, 6)
df[, s] <- sapply(df[, s], as.numeric)

df$Studio <- as.factor(df$Studio)

setwd("~/Documents/my-toolbox/5. Web Tools")
write.csv(df, "Scraper-BOM-Actors.csv")


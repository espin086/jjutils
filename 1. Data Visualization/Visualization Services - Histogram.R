###################
#JJ Visualization Library

#Histogram
x <- rnorm(1000)


jj.hist <- function(x){
        
        
        x <- as.numeric(x)
        bw <- (2 * IQR(x) / length(x)^(1/3))
                     
        library(ggplot2) 
        x <- as.data.frame(x)
             
        #Creating the histogram with density plot, rugs, and mean displayed
        m <- ggplot(x, aes(x = x))
        m <- m + geom_histogram(colour = "white",
                                fill = "light grey", 
                                binwidth = bw)
        m <- m + geom_rug(sides="b",col="red" ,alpha=.3)
        m <- m + geom_vline(aes(xintercept=mean(x, na.rm=T)),   
                            color="red", size=2,alpha=.3)
        m <- m + annotate("text", 
                        x = mean(x$x), 
                        y = 0, 
                        label = paste("Mean: ", round(mean(x$x), digits=1)))
        
        #Adding the plot theme
        jj_theme <- theme_bw(base_size = 12) + 
                theme(axis.line = element_line(colour = "black"),
                      panel.grid.major = element_blank(),
                      panel.grid.minor = element_blank(),
                      panel.border = element_blank(),
                      panel.background = element_blank()) 
        
        m <- m + jj_theme 
        
        m
        
}

jj.hist(x)

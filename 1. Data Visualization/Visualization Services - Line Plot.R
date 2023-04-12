x <- 1:100
y <- x + x*sin(x/5) + (x/2)*rnorm(100)

df <- as.data.frame(cbind(x,y))

jj.line <- function(x,y){
        p <- ggplot(df, aes(x = x, y = y))
        p <- p + geom_line(colour = "light grey")  
        p <- p + geom_rug(sides="l",col="red" ,alpha=.3)
   
     
        p <- p + geom_hline(aes(yintercept=mean(y)), 
                            colour = "red", 
                            size=2, alpha=.3)
        
        p <- p + annotate("text", 
                     x = 10, 
                     y = mean(y), 
                     label = paste("Mean: ", round(mean(y), digits=1)))
        
        
        jj_theme <- theme_bw(base_size = 12) + 
                theme(axis.line = element_line(colour = "black"),
                      panel.grid.major = element_blank(),
                      panel.grid.minor = element_blank(),
                      panel.border = element_blank(),
                      panel.background = element_blank())
        
        p <- p + jj_theme
        
        p
}

jj.line(df$x, df$y)

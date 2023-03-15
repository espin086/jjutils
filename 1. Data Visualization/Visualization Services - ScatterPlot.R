x <- 1:100
y <- 2*x + x*sin(x/5) + (x/2)*rnorm(100)

jj.scatter <- function(x,y){
        
        df <- as.data.frame(cbind(x,y))
        
        p <- ggplot(df, aes(x = x, y = y))
        p <- p + geom_point(colour = "black", size = 5)  
        p <- p + geom_rug(sides="bl",col="red", alpha=.3)
        p <- p +  geom_smooth(method='lm',formula=y~x)
        p <- p + geom_hline(aes(yintercept=mean(y, na.rm=T)), 
                            colour = "red", alpha=.3,
                            size=1)
        p <- p + geom_vline(aes(xintercept=mean(x, na.rm=T)),   
                            color="red", alpha=.3,
                            size=1)
        jj_theme <- theme_bw(base_size = 12) + 
                theme(axis.line = element_line(colour = "black"),
                      panel.grid.major = element_blank(),
                      panel.grid.minor = element_blank(),
                      panel.border = element_blank(),
                      panel.background = element_blank())
        
        p <- p + jj_theme
        
        p
}

jj.scatter(x, y)



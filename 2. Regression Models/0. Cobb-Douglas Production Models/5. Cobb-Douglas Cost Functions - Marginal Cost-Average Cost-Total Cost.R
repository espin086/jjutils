
#Calculating marginal cost and visualizing
chOut <- coef( costCDHom )[ "log(qTotalView)" ]
dat$margCost <- chOut * (dat$costCDHom / dat$qTotalView)
hist(dat$margCost, breaks = 20, col = "red", xlab = "Marginal Cost", ylab = "Number of Films", main="Marginal Cost of Producing Film")

#Marginal costs are greater than the price of output; profit maximization says continue to produce until marginal cost equals margina revenue (benefit), and since marginal cost is lower than marginal revenue most firms should continue to produce more output
compPlot( dat$pTotalView, dat$margCost, log = "xy" )

#Marginal cost based on the total output
plot( dat$qTotalView, dat$margCost )
plot( dat$qTotalView, dat$margCost, log = "xy" )

#Total, Marginal and Average Cost Curves
y <- seq( 0, max( dat$qTotalView), length.out = 200 )
chInt <- coef(costCDHom)[ "(Intercept)" ]
costs <- exp( chInt + chProps * log( mean( dat$pProps ) ) + 
                      chDirector * log( mean( dat$pDirector ) ) + 
                      chActors * log( mean( dat$pActors ) ) + 
                      chOut*log(y))

plot( y, costs, type = "l" )
# average costs
plot( y, costs/y, type = "l" )
# marginal costs
lines( y, chOut * costs / y, lty = 2 )
legend( "right", lty = c( 1, 2 ), legend = c( "average costs", "marginal costs" ) )


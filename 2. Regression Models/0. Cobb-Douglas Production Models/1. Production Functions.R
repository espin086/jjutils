####################
#Calculating average products

dat$apProps<- dat$qTotalView / dat$qProps
dat$apDirector <- dat$qTotalView / dat$qDirector
dat$apActors <- dat$qTotalView / dat$qActors

hist(dat$apProps, col = "red", main = "Output Per Prop", xlab = "Average Product of Props", ylab = "Number of Films")

hist(dat$apDirector, col = "red", main = "Output Per Director", xlab = "Average Product of Directors", ylab = "Number of Films")

hist(dat$apActors, col = "red", main = "Output Per Actor", xlab = "Average Product of Actors", ylab = "Number of Films")

####################
#Relationships between average products
plot(dat$apProps, dat$apDirector, main = "Relationship Between Average Products", xlab = "Average Product of Props", ylab = "Average Product of Director", col = "red")
plot(dat$apProps, dat$apActors, main = "Relationship Between Average Products",xlab = "Average Product of Props", ylab = "Average Product of Actors", col= "red")
plot(dat$apActors, dat$apDirector, main = "Relationship Between Average Products" , xlab = "Average Product of Actors", ylab = "Average Product of Director", col = "red")

####################
#Average product and firm size (as imperfectly measured by output)

plot(dat$qTotalView, dat$apProps,  main = "Relationship Between Average Products and Firm Size", xlab = "Total Viewership", ylab = "Average Product of Props", col = "red", log = "x")

plot(dat$qTotalView, dat$apDirector,  main = "Relationship Between Average Products and Firm Size", xlab = "Total Viewership", ylab = "Average Product of Directors", col = "red", log = "x")

plot(dat$qTotalView, dat$apActors,  main = "Relationship Between Average Products and Firm Size", xlab = "Total Viewership", ylab = "Average Product of Actors", col = "red", log = "x")

####################
#Examining Total Factor Productivity

#TFP by firm
dat$tfp <- dat$qTotalView / dat$X #output / index of inputs
hist(dat$tfp, col = "red", main = "Total Factor Productivity of Films", xlab = "TFP", ylab = "Number of Films")

#TFP by output
plot(dat$qTotalView, dat$tfp,  main = "Relationship Between TFP and Film Size", xlab = "Total Viewership", ylab = "TFP", col = "red", log = "x")


#TFP by input
plot(dat$X, dat$tfp,  main = "Relationship Between TFP and Film Size", xlab = "Index of Inputs", ylab = "TFP", col = "red", log = "x")

####################
#Some evidence that advisory services help
boxplot( tfp ~ adv, data = dat, main = "TFP Differences for Films with Consultant", xlab = "1 = Film with Consultant", ylab= "TFP", col = "red")

boxplot( log(qTotalView) ~ adv, data = dat, main = "Viewership Differences for Films with Consultant", xlab = "1 = Film with Consultant", ylab= "Total Views", col = "red")

boxplot( log(X) ~ adv, data = dat, main = "Input Differences for Films with Consultant", xlab = "1 = Film with Consultant", ylab= "Index of Inputs", col = "red")


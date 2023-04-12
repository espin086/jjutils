#Must run code that test assumptions first

hist( dat$pProps * dat$qProps / dat$cost ) 
lines(rep(chProps,2),c(0,100),lwd=3 ) 
hist( dat$pDirector * dat$qDirector / dat$cost )
lines(rep(chDirector,2),c(0,100),lwd=3 )
hist( dat$pActors * dat$qActors / dat$cost )
lines(rep(chActors,2),c(0,100),lwd=3 )
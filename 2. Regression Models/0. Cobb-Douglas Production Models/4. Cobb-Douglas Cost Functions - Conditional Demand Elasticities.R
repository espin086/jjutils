#Deriving the demand input elasticities - WARNING ASSUMES COBB-DOUGLAS
#
###############################
#Input elasticity for change in PROP price by 1%
e.props <- list()
e.props["own.elasticity"] <-as.numeric(costCD$coefficients[2] - 1)
e.props["cross.price.elasticity.directors"] <-as.numeric(costCD$coefficients[2])
e.props["cross.price.elasticity.actors"] <-as.numeric(costCD$coefficients[2])
e.props

#Input elasticity for change in DIRECTOR price by 1%
e.directors <- list()
e.directors["own.elasticity"] <-as.numeric(costCD$coefficients[3] - 1)
e.directors["cross.price.elasticity.props"] <-as.numeric(costCD$coefficients[3])
e.directors["cross.price.elasticity.actors"] <-as.numeric(costCD$coefficients[3])
e.directors

#Input elasticity for change in ACTORS price by 1%
e.actors <- list()
e.actors["own.elasticity"] <-as.numeric(costCD$coefficients[4] - 1)
e.actors["cross.price.elasticity.directors"] <-as.numeric(costCD$coefficients[4])
e.actors["cross.price.elasticity.actors"] <-as.numeric(costCD$coefficients[4])
e.actors


#Input elasticity for change in output by 1%
e.output <- list()
e.output["cross.price.elasticity.props"] <-as.numeric(costCD$coefficients[5])
e.output["cross.price.elasticity.directors"] <-as.numeric(costCD$coefficients[5])
e.output["cross.price.elasticity.actors"] <-as.numeric(costCD$coefficients[5])
e.output

#Elasticity of size - if cost increase by 1% then output would increase by 2.67%
1/as.numeric(costCD$coefficients[5])

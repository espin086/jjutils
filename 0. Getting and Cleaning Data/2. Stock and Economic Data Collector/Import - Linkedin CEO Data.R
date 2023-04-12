#########################
#Importing data from Linkedin.

require(devtools)
install_github("mpiccirilli/Rlinkedin")
require(Rlinkedin)

# To use the default API and Secret Key for the Rlinkedin package:
in.auth <- inOAuth()

my.connections <- getMyConenctions(in.auth)

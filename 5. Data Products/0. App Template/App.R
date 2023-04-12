library(shiny)

#########################################################
#UI
ui <- pageWithSidebar(headerPanel("Test"),
                      sidebarPanel(),
                      mainPanel()
                      )

#########################################################
#Server    
server <- function(input, output){}

#########################################################
#Shiny App Function
shinyApp(ui = ui, server = server)
        
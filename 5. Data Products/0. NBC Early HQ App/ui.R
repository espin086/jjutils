library(shiny)


shinyUI(pageWithSidebar(
        headerPanel("Predictive Model"),
        sidebarPanel(
                numericInput('DaystoHQ', 'Days to a High Quality Piracy Release', 0, min = 0, max = 100, step = 1),
                
                sliderInput('BO', "What is the total expected Box Office?", value = 10, min = 0, max = 500000000, step= 10000000),
                
                checkboxGroupInput('Genre', 'Genre of the Film', 
                                   c("Animation" = "1",
                                     "Adventure" = "2",
                                     "Comedy" = "3",
                                     "Drama" = "4",
                                     "Romantic Comedy" = "5",
                                     "Horror/Thriller" = "6")),
                
                checkboxGroupInput('Rating', 'Rating of Film', 
                                   c("G" = "G",
                                     "PG" = "PG",
                                     "PG-13" = "PG-14",
                                     "R" = "R"
                                      )),
                
                submitButton("Run Model")
                ),
        mainPanel(
                h3("Given the set of imputs..."),
                h5("Days to HQ:"),
                verbatimTextOutput("DaystoHQ"),
                h5("Film Genre:"),
                verbatimTextOutput("Genre"),
                
                h3("...a predictive model was created..."),
                
                h3("...here is the model prediction"),
                
                verbatimTextOutput("Prediction")
        )
))
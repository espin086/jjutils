library(stringr)
library(rvest)
library(dplyr)
library(magrittr)


make = 'honda'
model = 'accord'
npages = 10


zipcodes=sample(list("90210", "90670", "90650", "90806","92618", "90404"))
years=sample(list("2018", "2017", "2016", "2015", "2014"))


for(year in years){

for(zip in zipcodes){

url <- paste('https://www.truecar.com/used-cars-for-sale/listings/', 
             make, '/', 
             model ,
             '/location-', zip,
             '/year-',year,'-max/?page=', sep = "")

urls <- paste(url,1:npages,sep = "")

scrape <- function(pageno){
  try(
    read_html(urls[pageno]) %>% html_nodes('.col-xs-6.col-sm-8.no-left-padding') %>% html_text()
  )
}

long_list = scrape(1)
for(i in 2:npages){
  print(i)
  new_list = try(scrape(i))
  
  error = ("try-error" %in% class(new_list))
  
  if( error == FALSE ){
    long_list = c(long_list, new_list) 
  } else {
    break
  }
}



stats <- long_list
df <- as.data.frame(stats)
df$stats %<>% as.character()
df$price <- str_extract(df$stats, '\\$[0-9]*,[0-9]*') %>% 
  gsub('Price: |\\$|,', '', .) %>%
  as.numeric()
df$year <- str_extract(df$stats, '^[0-9]* ') %>% 
  as.numeric()
df$mileage <- str_extract(df$stats, 'Mileage: [0-9]*,[0-9]*') %>% 
  gsub('Mileage: |,', '', .) %>%
  as.numeric()

# a = df$stats[1]
df$trim <- str_extract(df$stats, '.*Mileage:') %>% 
  gsub('FWD|AWD|4x[24]|[24]WD|V6|4-cyl|^[0-9][0-9][0-9][0-9]|4dr|Automatic|Manual|Mileage:', '', ., ignore.case = T) %>% 
  gsub(make, '', ., ignore.case = T) %>% 
  gsub(model, '', ., ignore.case = T) %>% 
  trimws() 


df$awd <- grepl('AWD|4WD|4x4', df$stats, ignore.case = T) %>% as.numeric()
df$manual <- grepl('manual', df$stats) %>% as.numeric()
df$v6 <- grepl('V6', df$stats) %>% as.numeric()
df$location <- str_extract(df$stats, 'Location: .*Exterior:') %>% 
  gsub('Location: |Exterior:', '', .) %>% 
  trimws() 
df$ext <- str_extract(df$stats, 'Exterior: .*Interior:') %>% 
  gsub('Interior:|Exterior:', '', .) %>% 
  trimws() 
df$int <- str_extract(df$stats, 'Interior: .*VIN:') %>% 
  gsub('Interior: |VIN:', '', .) %>% 
  trimws() 
df$vin <- str_extract(df$stats, 'VIN: .*\\$') %>% 
  gsub('VIN: |\\$', '', .) %>% 
  substr(., 1, 17)
df$deal <- str_extract(df$stats, '\\$[0-9]*,[0-9]* below') %>% 
  gsub('below|\\$|,', '', .) %>% trimws() %>%
  as.numeric()


df = subset(df, select = -stats )




write.csv(df, file = paste0("../data/truecar/", make, '_', model,'_',year, '_', zip,'_',Sys.Date(), '.csv'), row.names=FALSE)
}
}

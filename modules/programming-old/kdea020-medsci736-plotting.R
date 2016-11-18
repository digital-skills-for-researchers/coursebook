#Visualisation stuff for MedSci736 class, 20/09/16
#Code by K. Deane-Alder, licensed under CC-BY 3.0 NZ

library(testthat) #import testthat library (thanks Hadley) for testing functions
                  #if not using testing, or testthat is not installed, comment this out, as well as the "test_that" function within parser()

workingdirectory <- setwd("/home/admin736/metabolomics-project/NLDL Data/") #replace with your own working directory

cat("Working directory is:", workingdirectory, "\n", "\n") # tells the user what the working directory is

parser <- function() { # init a function that will take user input and plot a graph based on their choice of file
  i <- readline(prompt = "Please enter the name of the file you wish to plot: (i.e. TEK0000.CSV) \t") #give the user an input prompt for the filename
  read.csv(i, header = FALSE) -> myfile #read the .CSV file using R's inbuilt function
  filename <- as.character(i) #saves the input (file name)
  metadata <- data.frame(key = myfile[1:10,1], value = myfile[1:10,2]) #metadata is split into a dataframe 
  readings <- data.frame(time = myfile[,4], voltage = myfile[,5]) #the appropriate columns from the file are split into a dataframe
  plot(readings$time*1000, readings$voltage, main = i, xlab = "Time (ms)", ylab = "Voltage (V)", type = "l", col = 2) #make the plot, including adjusting $time to milliseconds
  abline(v = 0, h = 0, col = 8) #draw faded grey lines, horizontally and vertically, at the 0,0 intercept for readability
  
  test_that("R has read the file correctly", { #testing for reading
    teststring <- readLines(i) #coerces the .CSV into a string
    splitted <- strsplit(teststring, ",") #splits the string by commas into a list
    expect_equal(as.numeric(splitted[[1]][5]), readings$voltage[1]) #checks to see if the list member corresponding to the expected value present in the data frame matches that value
  })

}

parser() #run the function immediately so the user just has to enter the name of the file they want to plot
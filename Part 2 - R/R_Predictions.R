# C742 - Task 1 - Part 2
# R Predictions
# By Rebecca Birmingham
# January 20th, 2019

#setwd("") #input proper workspare location

require(stats)
require(graphics)

# Import the population data - skipping the header as it is not needed
popData <- read.csv("nst-est2018-popchg2010_2018.csv", header = TRUE, skip = 1)

# Pulls the population estimates for just Colorado
popCol <- as.numeric(popData[10, c(7:15)]) 

# Create a vector of the years
years <- c(2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018)

# Create a linear model
coData2.lm <- lm(popCol ~ years)

# Create a barplot
barplot(popCol, names.arg = years, main = "Colorado Population 2010-2018", xlab = "Year", ylab = "Number of People", ylim = c(4000000,6000000), xpd = FALSE, col = c("lightblue"))

# Create a linear regression plot
plot(popCol ~ years, main = "Colorado Population 2010-2018", xlab = "Year", ylab = "Number of People")
abline(coData2.lm, col = "blue")

# Predict the population size for 2020
newData <- data.frame(years = 2020)
predict(coData2.lm, newData, interval = "prediction")

# Predict the population size for 2024 (5 years from now)
newData2 <- data.frame(years = 2024)
predict(coData2.lm, newData2, interval = "prediction")

# Output the linear model information
summary(coData2.lm)

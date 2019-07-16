#data processing 


#importing dataset
dataset = read.csv("Salary_Data.csv")

#splitting dataset to train set and test set
#install.packages('caTools') 
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split==FALSE)

#Fitting Simple linear Regression to the training set
regressor = lm(formula = Salary ~ YearsExperience, newdata = test_set)

#Visualising the Training set results
#install.packages("ggplot2")
library(ggplot2)
ggplot()+
  geom_point(aes(x=training_set$YearExperience, y=training_set$Salary),
             colour = 'red')+
  geom_line(aes(x = training_set$YearsExperience, y=predict(regressor,newdata=training_set)),
            colour = 'blue')+
  ggtitle("Salary vs Exp")+
  xlab("exp")+
  ylab("salary")
 
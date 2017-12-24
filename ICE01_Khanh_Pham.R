#Open the file car.test.frame.txt within R using read.table() 

workingdirectory = "C:\\Users\\Administrator\\Documents\\Master\\MSIS-5223-70250 - Programming for Data Sci - 8282017 - 159 PM\\Data for Tutorials and ICE\\Data"
setwd(workingdirectory)
template = paste(workingdirectory,"\\car.test.frame.txt", sep="")
datafile = read.table(template,header=T, sep="\t" )

#Find out what the column header names are
names(datafile)

#Determine the number of rows 
nrow(datafile)

#Determine the number of columns 
ncol(datafile)

#Test your dataframe to determine which columns are categorical 
datafile[,sapply(datafile,is.factor)]

#How many unique values does Type have

unique(datafile$Type)

# How many unique values does Country have?
unique(datafile$Country)

#What is the value of row 57, column 3? 
datafile[57,3]

#What are the values for row 24? 
datafile[24,]

#Using three different methods, select row 29 with columns 1, 2, 3
#method 1
datafile[29,1:3]
#method 2
datafile[29,c(1,2,3)]
#method 3
datafile[29,c("Price","Country","Reliability")]


#Using two different ways, select row 45 with columns 3 and 7
#method 2
datafile[45,c(3,7)]
#method 3
datafile[45,c("Reliability","Disp.")]

#Create a new dataframe for the column HP using two different methods
HP.datafile1 = datafile[,8]

HP.datafile2 = datafile$HP

HP.datafile

#Select compact cars that have a reliability greater than and equal to 4. 
Compact_Car = datafile[datafile$Type == "Compact" & datafile$Reliability >=4,1:8]

#Test Dataframe from  missing value
#True means it is complete; no missing value
complete.cases(Compact_Car)
Compact_Car = na.omit(Compact_Car)
Compact_Car

#Find compact cars that have a reliability greater than and equal to 3 from Japan, but not from the US 
JP = datafile[datafile$Type == "Compact" & datafile$Reliability >= 3 & datafile$Country == "Japan",1:8]
JP

#How many cars are manufactured in the USA/Japan? 
car_in_USA.JA = datafile[datafile$Country == "Japan/USA",]
nrow(car_in_USA.JA)

#How many cars are manufactured in the US or Japan? 
car_USA_JA =  datafile[datafile$Country == "USA" | datafile$Country == "Japan",]
car_in_USA.JA
nrow(car_USA_JA)

#How many cars are manufactured in the US or Japan with a reliability greater than and equal to 4?
car_reliability =  datafile[(datafile$Country == "USA" | datafile$Country == "Japan") & datafile$Reliability == 4,]
car_reliability = na.omit(car_reliability)
car_reliability
nrow(car_reliability)

#Create a subsample of 70% of your data 
subsample = floor(nrow(datafile) * 0.7)
subsample
x = 1:60
subsample = datafile[sample(subsample, replace = F),]
subsample

#Create samples for a 8-fold cross validation test; save each subsample as a new dataframe 

#Browse for the file
datafile = read.table(file.choose())
names(datafile)

#dataframe
datafile

#edit
datafile = edit(datafile)

#unique Value does Type has?
summary(datafile)

try(data(package="psych"))

#Remove the columns of interest
View(data)



#Open the file car.test.frame.txt within R using read.table() 

workingdirectory = "C:/Users/Administrator/Documents/Master/MSIS-5223-70250 - Programming for Data Sci - 8282017 - 159 PM/Homework"
setwd(workingdirectory)
Personnel = paste(workingdirectory,"\\CaliforniaHospitalData_Personnel.txt", sep="")
Hospital =paste(workingdirectory,"\\CaliforniaHospitalData.csv", sep="")
df = read.table(Personnel,header=T, sep="\t" )
df1 = read.csv(Hospital,header =T, sep =",")
df
df1
View(df1)
View(df)
#Merge two table Personnel and Hospital
df3 = merge(df,df1, all=FALSE)
df3
View(df3)
names(df3)



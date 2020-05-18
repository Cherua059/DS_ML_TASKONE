#provided in .txt file
# Attributes for student-math.csv (Math course) dataset:
# 1 school - student's school (binary: "GP" - Gabriel Pereira or "MS" - Mousinho da Silveira)
# 2 sex - student's sex (binary: "F" - female or "M" - male)
# 3 age - student's age (numeric: from 15 to 22)
# 4 address - student's home address type (binary: "U" - urban or "R" - rural)
# 5 famsize - family size (binary: "LE3" - less or equal to 3 or "GT3" - greater than 3)
# 6 Pstatus - parent's cohabitation status (binary: "T" - living together or "A" - apart)
# 7 Medu - mother's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
# 8 Fedu - father's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
# 9 Mjob - mother's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")
# 10 Fjob - father's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")
# 11 reason - reason to choose this school (nominal: close to "home", school "reputation", "course" preference or "other")
# 12 guardian - student's guardian (nominal: "mother", "father" or "other")
# 13 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
# 14 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
# 15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
# 16 schoolsup - extra educational support (binary: yes or no)
# 17 famsup - family educational support (binary: yes or no)
# 18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
# 19 activities - extra-curricular activities (binary: yes or no)
# 20 nursery - attended nursery school (binary: yes or no)
# 21 higher - wants to take higher education (binary: yes or no)
# 22 internet - Internet access at home (binary: yes or no)
# 23 romantic - with a romantic relationship (binary: yes or no)
# 24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
# 25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
# 26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
# 27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
# 28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
# 29 health - current health status (numeric: from 1 - very bad to 5 - very good)
# 30 absences - number of school absences (numeric: from 0 to 93)
# 31 G1 - first period grade (numeric: from 0 to 20)
# 31 G2 - second period grade (numeric: from 0 to 20)
# 32 G3 - final grade (numeric: from 0 to 20)





#importing the liabraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

#changing the working directory to current direntory, where the code and the .csv files are present
os.chdir(os.path.dirname(os.path.abspath("__file__")));

#reading the data and creating a datframe
data = pd.read_csv(r"student-math.csv",sep=';',quotechar='"');
dataframe = pd.DataFrame(data,columns=['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','guardian','traveltime','studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences','G1','G2','G3']);

#creating a new column which is the sum of G1,G2 and G3 elements
final_grade = [];
for i in range(0,len(data)):
    sum = data.G1[i] + data.G2[i] + data.G3[i];
    final_grade.append(sum);
    sum=0;
dataframe['final_grade'] = final_grade;

#removing the colums
dataframe = dataframe.drop(columns=['G1','G2','G3']);


#replacing columns with binary values with 1 and 0
dataframe.replace(to_replace=['YES','yes','Yes','GP','M','U','LE3','T'],value=1,inplace=True);
dataframe.replace(to_replace=['no','NO','No','MS','F','R','GT3','A'],value=0,inplace=True);

#creating a list for plotting
l1=dataframe['studytime'].tolist() #x-axis
l2=dataframe['final_grade'].tolist() #y-axis


#scatter plot
plt.figure()
plt.scatter(l1,l2,c=l1,cmap='RdBu',marker= "o",s=10);
plt.xlim(0,5);
plt.xlabel('STUDY-TIME');
plt.ylabel('FINAL-GRADE');
cbar = plt.colorbar(orientation="horizontal");
cbar.set_label('study-time');
plt.clim(0,5);


#final plot to compare the two plots
plt.figure()
plt.subplot(2,1,1);
plt.scatter(l1,l2,c=l1,cmap='RdBu',marker= "o",s=10)
plt.subplot(2,1,2);
sns.boxplot(x='studytime',y='final_grade',data=dataframe) 
# use of seaborn for boxplot as the boplot by pandas
# was not being displayed in the subplot windows

#box plot using pandas
plt.figure()
dataframe.boxplot(column='final_grade',by='studytime')
plt.show()
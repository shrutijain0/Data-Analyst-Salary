# Data Analyst Salary Predictor : SUMMARY
*This is an End to End project for Data Analyst salary prediction.*
* Created a Project Thats helps you to predict Data Analyst salary .
* I have cleaned the dataset and made it model ready and to perform prediction.
* Performed Exploratory Data Analysis(EDA) on the data set to understand it and make some accurate discovery.
* Builded Two Model and found the best fit and had better performance
* Deployed the project using Flask API.

## DATA SET:
This data set is taken from Kaggle where and it is Scrapped from GlassDoor platform which is famous for it employment service and 
data has these features 
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company Name
* Location
* Headquarters
* Size
* Founded
* Type of ownership
* Industry
* Sector
* Revenue
* Competitors
* Easy Apply
## DATA CLEANING:
In this stage of project i had cleaned data and made specific changes like 
* Simplified the **Job Title** into a smaller version of it.
* Made salary feature by removing these **Glassdoor Estimate** and **k or $** for fitting it to a mdoel.
* Took the length of the description instead of taking the description as the whole.
* Made **Level** feature to describe the seniority of the job position.
* Created **Min salary** and **Max salary** feature to better understand the data and for model performance.
* Created a Avg Salary feature which we will use in prediction.
* And made many more changes which can be viewed in the DA Cleaned data csv.
##  Exploratory Data Analysis(EDA):
Performed Exploratory Data Analysis on the cleaned data and got a lot of insights , few of them are 
<img src="https://github.com/shrutijain0/Data-Analyst-Salary/blob/main/EDA/heatmap.png" width="400" height="400"> <img src="https://github.com/shrutijain0/Data-Analyst-Salary/blob/main/EDA/title.png" width="400" height="400">
<img src="https://github.com/shrutijain0/Data-Analyst-Salary/blob/main/EDA/sector.png" width="400" height="400">
* These are some example of the insights gained from the cleaned dataset.
## MODEL BUILDING:
For this project i have used two different models and compared its MAE to figure out which one most accurate and has better performance on this data.
used MAE because as all the individual differences are weighted equally in the average
#### ***-Linear Regression:*** attempts to model the relationship between two variables by fitting a linear equation to observed data.
#### ***-RandomForestRegressor:***  it is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.
## PERFORMANCE:
The performance of the model was based on MAE of the model and Random Forest Regressor performed way better than Linear Regression.
* ***Linear Regression***= 406.2
* ***RandomForest Regressor***=15.8
#### As you can linear regression's MAE is very high because of many features and there dummie features which is alot for linear regression and random forest has performed way better. which means **MAE ~ $15K** .
## DEPLOYMENT:
I have deployed my project using FLASK API and which take request and gives you a the estimated salary of an data analyst in accordance to your input data.
### SPECIAL THANKS TO KEN JEE: 
Ken Jee is an data scientist and a youtuber and he has many data science related video on his channel and he had made a series of DATA SCIENTIST salary project which has helped a lot in this project and his deployment video has inspecific helped me a lot to deploy this project. i would reccomend you to go through his channel for some amazing data science stuff.
# Resource:
* Ken Jee youtube channel :https://www.youtube.com/channel/UCiT9RITQ9PW6BhXK0y2jaeg
* ken jee project series :https://youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t
* DataSet: https://www.kaggle.com/andrewmvd/data-analyst-jobs
 
#### LINKDIN : https://www.linkedin.com/in/shruthi-jain-81b4571ab/

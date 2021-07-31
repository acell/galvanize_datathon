I worked on this project resulting in this presentation (https://docs.google.com/presentation/d/1ta3rZ7aWH2cUAPOIGiI1mrmQeq82V-I-5URdA6yM3OA/edit?usp=sharing) as part of the Galvanize Hackathon in 7/2021.

The data is from NYISO (https://www.nyiso.com/energy-market-operational-data)

All work was done in a jupyter notebook, but the main functions that are used to get the data are also in a python file.

Work included:
* Downloading and unzipping .zip files
* Aggregating the CSVs into dataframes
* Creating a dataframe of unscheduled outages by removing scheduled outages from all real-time outages
* Performing unscheduled outage EDA
* Creating time series-type features with the load data (moving averages, standard deviations, minimums/maximums)
* Training random forest classification and logistic regression models to predict the likelihood of each 5min interval to have 1+ blackouts
* Assessing results, looking at area under the ROC curve and outage likelihood in high- and low- predicted risk buckets

# Vehicles_Data_Analysis

1. First the time Trip-Info.csv data is changed to datetime[ns] with 01_preprocessing.py and stored in trips.csv so later it can be compared easily!
2. No other Data Unit conversion as it may increase unnecessary time and storage of new files.

## **The query_function**
1. It takes two arguments i.e. the start and end time between which we want the data.
2. It takes all the CSV file one by one from the EOL-dump folder and read that file as a pandas data frame
3. Now the function filters the data frame and takes data only within the limits of time.
4. Now we are good to get some of the values from this filtered data frame like License plate number, Distance, Average Speed, Number of Speed Violations
and if the data frame would be empty then we continue to check for other vehicles' data.
5. Similarly now the function filters the trip.csv data frame within the limits given by the user and takes the values Number of Trips Completed and Transporter Name from the data frame
6. Now to use the solution as an API I used Flask and the Flask can be run with the function app.py
7. The page UI takes 2 inputs as shown in the image
![0](https://github.com/wasiongit/Vehicles_Data_Analysis/assets/84765303/fbd6b719-1e23-4e1a-ac44-7608886d7ce6)

8. After submission it gives the data in a structured format with a link to download the Excel output also.

![2](https://github.com/wasiongit/Vehicles_Data_Analysis/assets/84765303/d05f43ea-0900-4716-90a7-d8775f8e4ac2)

9. It can also be used as an API, sample usage given in the function api_test.py

Thanks for your time.



  

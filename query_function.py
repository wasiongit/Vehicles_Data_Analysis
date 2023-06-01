import pandas as pd
from datetime import datetime
import os
import math


# this is the function to calculate the distance
def haversine(lat1, lon1, lat2, lon2):
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c


def main_query_f(input_time1,input_time2):
    time1 = datetime.fromtimestamp(input_time1)
    time2 = datetime.fromtimestamp(input_time2)

    # reading the trip csv out of the loop
    trips_df=pd.read_csv('trips.csv',index_col=0)

    vehicles=os.listdir('EOL-dump')
    data=[]
    print('Total no. of vehicles ',len(vehicles))
    i=1 #i is declared to just get the status
    for vehicle in vehicles:
        print(i)
        print(vehicle)
        raw_df=pd.read_csv(f'EOL-dump/{vehicle}',index_col=0)
        filterd_df=raw_df.query(f'tis >{input_time1} and tis<{input_time2}')

        if filterd_df.count()[0]==0:
            # if No Data found
            i+=1
            continue
        license_plate_no=filterd_df['lic_plate_no'].to_list()[0]
        avg_speed=filterd_df['spd'].dropna().describe()['mean'] #droping null values
        n_over_speed=filterd_df.query('osf==True').count()[0]

        filterd_df=filterd_df.sort_values('tis',ignore_index=True)
        distances=[]
        lat1=filterd_df['lat'][0]
        lon1=filterd_df['lon'][0]
        for ind in filterd_df.index:
            lat2=filterd_df['lat'][ind]
            lon2=filterd_df['lon'][ind]
            distances.append(haversine(lat1,lon1,lat2,lon2))
            # updating the values
            lat1=lat2
            lon1=lon2

        filterd_df['Distances']=distances
        total_distance=filterd_df['Distances'].sum()

        ########################################################################################################################
        # form trip.csv
        filtertrips_df=trips_df.query(f"vehicle_number=='{license_plate_no}'")
        filtertrips_df=filtertrips_df.query(f'date_time >"{time1}" and date_time<"{time2}"')


        if filtertrips_df.count()[0]==0: #if no data found within the limits
            i+=1
            continue
        no_of_trips=filtertrips_df.count()[0]
        transporter_name=filtertrips_df['transporter_name'].to_list()[0]
        ##################################

        row=(license_plate_no,total_distance,no_of_trips,avg_speed,transporter_name,n_over_speed)
        data.append(row)
        i+=1
    
    if len(data)==0:
        return 'No data Found in the Given Range'

    output_df=pd.DataFrame(data)
    output_df.columns=['License plate number','Distance','Number of Trips Completed','Average Speed','Transporter Name','Number of Speed Violations']
    output_df.to_excel('static/output.xlsx')
    return True

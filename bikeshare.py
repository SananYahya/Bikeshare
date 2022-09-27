import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


         
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        
        city = input('Which city do would you like to explore: chicago, new york city or washington?: ').lower()
        
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('You did select the wrong city! Please select chicago, new york city or washington')
            continue
    
    while True:
        month = input('Select the month from january to june: ').lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            
            break
        else:
            print('You did select the wrong month! Please write again')
            continue
    
    while True:
        day = input('Select the week day : ').lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print('You did select the wrong week day! Write again: ')
            continue


    print('-'*40)
    
    return city, month, day




def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    

    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        
        
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]
        
    
    

    
    
    return df


def time_stats(df):
    

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print('The most common month is: {}'.format(months[month-1]))
    
    
    day = df['day_of_week'].mode()[0]
    print('The most common day of week is: {}'.format(day))

    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    print('the most common start station is ', df['Start Station'].value_counts().idxmax())
        
    # TO DO: display most commonly used end station
    print('the most common end station is ', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    start_and_endpoint  = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(start_and_endpoint)

    
    print('-'*40)        

    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 3600
    print('Total travel time is {} hours'.format(total_travel_time.round()))
    
    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print('Mean travel time is {} seconds'.format(mean_travel_time.round()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 

                
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if 'Birth Year' in (df.columns):
        least_recent_year = df['Birth Year'].min()
        print('The earliest year of birth is {}'.format(int(least_recent_year)))
        most_recent_year = df['Birth Year'].max()
        print('The most recent year of birth is {}'.format(int(most_recent_year)))
        most_common_year = df['Birth Year'].mode()[0]
        print('the most common year of birth is {}'.format(int(most_common_year)))
        


    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print(user_types_count)


    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        gen_counts = df['Gender'].value_counts()
        print(gen_counts)
    

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
def raw_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows """
    raw = input('Would you like to diplay raw data? ')
    if raw.lower() == 'yes':
        i = 0
        while True:
            print(df.iloc[i: i+5])
            i += 5
            ask = input('Next 5 raws? ')
            if ask.lower() != 'yes':
                break


                
                
                
                
def main():
                
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() !='no' and restart.lower() !='yes':
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() !='yes':
            break
                
                
            
            

                    
      

                
                
            
            

            
                
                   
           
        
        
            
            
            

            
        
       
           
                
        


if __name__ == "__main__":
    main()
    
    

    
    

    

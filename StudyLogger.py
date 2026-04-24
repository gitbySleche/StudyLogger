from datetime import datetime

current_date = datetime.today()

with open("Study_Log.txt", "a+") as log:

    log.seek(0)
    lines = log.readlines()

    if lines:
        
        last_line = lines[-1]
        last_date_string = last_line[:11]  
        if last_line[-1] == "-":

            start = last_line[-6:-1]
            start_time = datetime.strptime(start, '%H:%M') #turn a string into a datetime object 
            last_date = datetime.strptime(last_date_string, '%d-%b-%Y') #turn a string into a datetime object 
            end_time = current_date.strftime('%H:%M')  #turn a datetime object into a string
            total_time = datetime.strptime(end_time, '%H:%M') - start_time #creates an equal datetime object from the previous turned string so it can be subtracted with start_time datetime object 
            current_date_shrinked = datetime(current_date.year, current_date.month, current_date.day) #just get these 3 out of current_date

            if current_date_shrinked > last_date:
                
                total_time = current_date - last_date
                total_time_D = total_time.days 
                total_time_H = total_time.seconds // 3600
                total_time_M = (total_time.seconds % 3600) // 60
        
                log.write(f'({current_date.strftime('%H:%M, %d-%b-%Y')} {total_time_D} days, {total_time_H} hours and {total_time_M} minutes)')


            else:
                
                total_time_H = total_time.seconds // 3600
                total_time_M = (total_time.seconds % 3600) // 60
                log.write(f'{end_time} ({total_time_H} hours and {total_time_M} minutes)') #write the rest of the info into the file
                
                if input("Would you like to comment on your last session?(y/n) ").lower() == "y":
                    
                    comment = input("Go ahead: ")
                    log.write(f', Comments: "{comment}".')
                    
                print("Last Session Ended. Log updated.")


    if input("Start new Session?(y/n) ").lower() == "y":  
        study_topic = input("What do you plan on studying today? ")
        log.write(f'\n{current_date.strftime('%d-%b-%Y')}, "{study_topic}", start/end: {current_date.strftime('%H:%M')}-')
        print("New Session Started.")

    else:
        print('No session started.')
    
 

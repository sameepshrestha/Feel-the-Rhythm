# Model Documentation

Please use this file to document your work.
we have added some data after preprocessing the features from the public dataset. Full code to extract these lists has been added to the 
explainability report

These data name and information about them are listed below
    1  distion1 = dictionary containing the number of days each employee has worked in a month for all years 
            distion1[employee]= [[2014],[2015],[2016],[2017],[2018],[2019]] 
            where,
            [2014] =[days worked in its months] for example [0,0,0,12,24,21,12,12,12,12,12,12]

    2  diff = distionary containing the regular working hour range of each employee 
            diff[employee] =[7,14] where employee works from 7 to 14 in regular basis and anything except this is an exception

    3  lists a_2014,a_2015,a_2016,a_2017,a_2018,a_2019,a_2020  = each of the lists contains the employee which started working from the   year decorated in their name
           for example a_2014 = contains all the unique emplyoee who started working on the year 2014 assuming no work before 2014

    4  WORK_DESC_TOP = contains the list of the top 50 work_desc after data processing 

    5  workk_no = list containg the top 57 preprocessed work number
    6  summer and winter where the month is grouped into two categories

There are many functions carrying out different tasks and these functions whith their work is listed below-

    1  work_alpha = preprocesses the wor_desc i.e removes white spaces, any special character 
    2  season     = returns summer if is in the list summer and returns winter if is in the list winter
    3  double_mgmt = combines the different classes of the work_desc 
            example = all staring with tcs and containing pole jobs is listed as "TCSpole" and all other are listed as "TCS" 
    
    4  looper      = returns the number of days a employee works in a month according to the disctionary distion1 for each employee for every year
    5  top_work_desc_feat = returns the work_desc if in the list work_desc_top else returns "other"
    6  sleep_hour  = the biological sleeping time for average adult was set to be from 10 pm to 6 am which accounts to total hours of 8 
                    the remaining time was set into category "Day time" 
    7  job_hour    = extracts the alphabet present in the work_no and if no alphabet return "number"
    8  year desc   = returns 2014 if the employee is present in a_2015 and similarly 2015 if present in a_2015
    9  sunrise and sunset = extracts the sun shisne and sunset time for that day
    10 EmpNo_Anon_categorical  =  extracts the first two digit from the EmpNo_Anon
    11 Funcc = returns 0 if works in reguar shift for an employee as seen in diff and returns 1 if work is done out of regular working range


# year_num 
year_no is the year the employee started assuming 2014 as the earliest year 
year_num = year_no - year , where year is the year of current job, which gives the age or experience of the workes as 1,2,3 years
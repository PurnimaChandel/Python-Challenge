import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvpath = os.path.join('employee_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)
    
    new_empid = []
    first_names= []
    last_names= []
    dobs =[]
    SSNs =[]
    states= []
    
    for row in csvreader:
        emp_id = row[0]
        new_empid.append(emp_id)
        first_name = row[1].split(" ")[0]
        first_names.append(first_name)
        last_name= row[1].split(" ")[1]
        last_names.append(last_name)
        year = row[2].split("-")[0]
        month = row[2].split("-")[1]
        day =  row[2].split("-")[2]
        dob = month + "/"+ day + "/" + year
        dobs.append(dob)
        split_SSN = row[3].split("-")[2]
        SSN = "***-**-"+ split_SSN
        SSNs.append(SSN)
        abr_state = us_state_abbrev[row[4]]
        states.append(abr_state)
        
new_csv = zip(new_empid, first_names,last_names,dobs,SSNs,states)
output_file = os.path.join("new_"+ "employee_data.csv")
with open(output_file, 'w') as datafile:
    csvwriter = csv.writer(datafile, delimiter= ",")
    csvwriter.writerow(["Emp Id", "First Name", "Last Name", "DOB", "SSN","States"])
    csvwriter.writerows(new_csv)

new_path = os.path.join('new_employee_data.csv')
with open(new_path, 'r') as file:
    new_file = csv.reader(file, delimiter= ",")
    
    for item in new_file:
        print(item)
        
    

        
        
        
        
        
    
    
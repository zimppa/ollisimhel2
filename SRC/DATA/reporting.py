#Reporting software:Create a software that reads the daily/weekly consultant time tracking from PostgreSQL database table
#And writes a report to a text file. This report is then uploaded to storage account as a blob for your team leader to read. 
#The Scenario 1 reporting software will be run manually from commandline.

import psycopg2
from config import config

# Database connect
def main():
    try:
           # Connect
            params = config()  # Get the database parameters
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

           # SQL query
            cur.execute("SELECT consultantName, customerName, startTime, endTime, lunchbreak  FROM time_management;") 
            time_tracking_data = cur.fetchall()

           # Generate the report
            report = generate_report(time_tracking_data)

           # Write the report to a text file
            with open('consult_time_tracking_report.txt', 'w') as f:
               f.write(report)

            print("Report generated successfully!")

    except (Exception, psycopg2.Error) as error:
           print("Error:", error)

    finally:
           if conn:
               cur.close()
               conn.close()
               
#report generation
def generate_report(data):
    report = "Consultant Time Entry\n--------------------\n"

    for entry in data:
        consultantName, customerName, startTime, endTime, Lunchbreak = entry
        report += f"Consultant name: {consultantName}\n"
        report += f"Customer Name: {customerName}\n"
        report += f"Time started working: {startTime}\n"
        report += f"Time stopped working: {endTime}\n"
        report += f"How long lunchbreak they had?: {Lunchbreak}\n"
        report += "--------------------\n"  
    return report 

if __name__ == "__main__":
       main() 
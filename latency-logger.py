import re
import subprocess
import csv
from datetime import datetime


sites = ['google.com', 'github.com', 'reddit.com', 'stackoverflow.com']

regex = r"time=(\d+\.?\d*) ms"

log_file = "ping_log.csv"

with open(log_file,'a+',newline="") as file:
    writer = csv.writer(file)

    file.seek(0)
    
    if file.read(1) == "":
        writer.writerow(['timestamp  ','website  ','ping_ms  '])

        for site  in sites:
            print("Pinging {}...".format(site))

            result = subprocess.run(['ping','-c','4',site],text=True,capture_output=True)

            output = result.stdout

            times = re.findall(regex,output)

            if times:
                avg_ping = sum(map(float,times)) / len(times)

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                for t in times:
                    writer.writerow([timestamp, site, t])

                print("Average ping to {}: {:.2f} ms".format(site,avg_ping))
            
            else:
                print("Could not find ping times for {}".format(site))


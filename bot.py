import tempfile
import dns.resolver
import csv
import shutil

tempfile = tempfile.NamedTemporaryFile(mode='w', delete=False)
total_invalid = 0
csv_src = raw_input('CSV location: ')
fields = ['First Name', 'Last Name', 'Full Name', 'Email Address', 'Timezone', 'IP Address', 'Subscribed', 'Added at',
          'Updated at']
firstLine = True
with open(csv_src, 'r') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
            try:
                result = dns.resolver.query(row["Email Address"].split("@")[1], 'MX')
            except:
                if firstLine:
                    firstLine = False
                else:
                    total_invalid = total_invalid + 1
                    row["Subscribed"] = "false"
                    print(str(total_invalid - 1) + " invalid Email found!")

            row = {'First Name': row['First Name'], 'Last Name': row['Last Name'], 'Full Name': row['Full Name'],
                   'Email Address': row['Email Address'],
                   'Timezone': row['Timezone'], 'IP Address': row['IP Address'], 'Subscribed': row["Subscribed"],
                   'Added at': row['Added at'],
                   'Updated at': row['Updated at']}
            writer.writerow(row)

shutil.move(tempfile.name, "newlist.csv")






'''Script that checks for new skype files in hdfs and insert those data into hive table
   Must have database and table skype_bot skype_data already created
'''
import subprocess
import re
skype_files = subprocess.check_output(["hdfs","dfs", "-find","*.tsv" ]).decode("utf-8").rstrip().split("\n")

#open file that stores the time hive was last updated. Insert new data into if new files were added in hdfs since then
with open("saved_time", "r+") as f:
        hive_last_update_time = float(f.read().rstrip())
        print("Last time hive was update: {}".format(hive_last_update_time))
        files_since_last_update = list(filter(lambda x : float(re.findall("\d+\.\d+", x)[0]) > hive_last_update_time ,skype_files))
        if(len(files_since_last_update) != 0):
                for myfile in files_since_last_update:
                        hql_command = "load data inpath \'" + myfile + "\' into table skype_bot.skype_data;"
                        subprocess.call(["hive","-e",hql_command])
                        print("Loaded data from file " + myfile + " into table skype_data")
                f.seek(0)
                f.write(str(re.findall("\d+\.\d+",files_since_last_update[-1])[0]))
                f.truncate()
        else:
                print("No new file detected. Database up to date\n")


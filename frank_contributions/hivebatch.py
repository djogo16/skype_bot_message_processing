import subprocess
import re
skype_files = subprocess.check_output(["hdfs","dfs", "-find","*.tsv" ]).decode("utf-8").rstrip().split("\n")
print(skype_files)
with open("saved_time", "r") as f:
        hive_last_update_time = float(f.read().rstrip())
        print(hive_last_update_time)
        files_since_last_update = list(filter(lambda x : float(re.findall("\d+\.\d+", x)[0]) > hive_last_update_time ,skype_files))
        if(len(files_since_last_update) != 0):
                for myfile in files_since_last_update:
                        hql_command = "load data inpath \'" + myfile + "\' into table skype_bot.skype_data;"
                        subprocess.call(["hive","-e",hql_command])
                        print("Loading data from file " + myfile + " into table skype_data")
                #f.write(str(re.findall("\d+\.\d+",files_since_last_update[-1])[0]))
        else:
                print("No new file detected. Database up to date\n")


# This document is prepared by Aysenur Toptan
# to output in .csv format
import csv


## UNIT TEST RESULTS ===========================================================
with open('write_toCSV.csv', "w") as fp:
    
    ## OUTPUT RESULTS |------------
    # write to csv file
    a = csv.writer(fp, delimiter=',')
    wdata = [['xxx','xxx','xxx','xxx','xxx'],
             ['xxx.','xxx','xxx','xxx','xxx']]
        
    wdata.append([1,'xxx','xxx','xxx','xxx'])
    wdata.append([2,'xxx','xxx','xxx','xxx'])
    wdata.append([3,'xxx','xxx','xxx','xxx'])
    wdata.append([4,'xxx','xxx','xxx','xxx'])
    wdata.append([5,'xxx','xxx','xxx','xxx'])


    # Close the .csv file
    a.writerows(wdata)

fp.close()

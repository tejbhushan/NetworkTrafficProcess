#requirements<br />
Install Python3<br />
Install pip - sudo apt install python3-pip 

#run<br />
python flow_log_parser.py --log_file flow_logs.txt --lookup_file tag_lookup_table.csv

#assumptions<br />
Browsing on the log, it resembles to AWS flow log format v2. So, program works for the v2 and not for custom formats or compressions.<br />
Assuming - 1 (ICMP), 6 (TCP) and 17 (UDP) only for now.<br />
Unmatching dstport and protocol combinations are considered "Untagged."

#tests<br />
Test carried out on input file provided.<br />
Logs lines with missing fields will be rejected.

#code analysis<br />
The program is can be optimized for handling large log files by using a streaming approach (TODO) to process flow logs line-by-line, minimizing memory usage. Or mutliprocessing for faster processing. <br />
The lookup table is stored in a dictionary for O(1) lookup time.<br />
The program is now can efficiently processing up to 10 MB log files with a lookup table of 10,000 entries.
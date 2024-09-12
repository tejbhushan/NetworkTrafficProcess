#requirements
Install Python3
Install pip - sudo apt install python3-pip

#run
python flow_log_parser.py --log_file flow_logs.txt --lookup_file tag_lookup_table.csv



#assumptions
Browsing on the log, it resembles to AWS flow log format v2. So, program works for the v2 and not for custom formats or compressions.
Assuming - 1 (ICMP), 6 (TCP) and 17 (UDP) only for now.
Unmatching dstport and protocol combinations are considered "Untagged."

#tests
Test carried out on input file provided
Logs lines with missing fields will be rejected.

#code analysis
The program is can be optimized for handling large log files by using a streaming approach (TODO) to process flow logs line-by-line, minimizing memory usage. Or mutliprocessing for faster processing. 
The lookup table is stored in a dictionary for O(1) lookup time.
The program is now can efficiently processing up to 10 MB log files with a lookup table of 10,000 entries.
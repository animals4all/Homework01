log_file = open("um-server-01.log.txt")

def sales_reports(log_file):
	for line in log_file:
	    line = line.rstrip()
	    day = line[0:3]
	    if day == "Mon":
	        print line

def main(log_file):
	sales_reports(log_file)


if __name__ == '__main__':	
	main(log_file)

'''
Goal: Automate log filtering and summarizing
'''


from datetime import datetime

def error_logging(fileName):
    error_count = 0
    warning_count = 0
    error_list = []
    try:
        with open(fileName, "r") as f:
            for line in f:
                if "ERROR" in line:
                    error_count +=1
                    error_list.append(line)
                elif "WARNING" in line:
                    warning_count +=1
                    error_list.append(line)
    except Exception as e:
        print(e)
    
    if len(error_list) > 0:
        try:
            with open("alert_log.txt", "w") as f:
                for line in error_list:
                    f.write(line)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M") 
                f.write(f"{timestamp}: FOUND {error_count} ERRORS and {warning_count} WARNINGS")
        except Exception as e:
            print(e)


def main():
    fileName = input("Enter a file name to get the summarized report: ")
    error_logging(fileName)


if __name__ == "__main__":
    main()
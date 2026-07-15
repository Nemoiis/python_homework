import traceback

running = True
counter = 0

try:
    with open('diary.txt', 'a') as diary:
        while running:
                
            if counter == 0:
                response = input("What happened today?\n")
                print(response)
                diary.write(response + "\n")
                counter += 1

            else:
                response = input("What else?\n")
                if response == "done for now":
                    diary.write(response + "\n")
                    running = False
                
                else:
                    print(response)
                    diary.write(response + "\n")
                    counter += 1

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")




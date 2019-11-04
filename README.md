# Personal_Log
Personal Log Class for Python
Still working

To do list  
1.0. Define Log Class.   
1.1. Create Skelecton for Log class using singleton pattern.  
1.2. Create Constructor   
1.3. Create Destructor  
1.4. add member functions as belows:  
    ・write_log_msg("function.No", "Msg")    
    ・read_log_msg("function.No")  
    ・logger_handler()  
    ・read_log_unit("log_file_name")   
    ・write_log_diff("File_name")  
    
ref for text parsing : https://sancs.tistory.com/21

로그 에서 차분 값을 산출할 때는 다음과 같은 데이터 구조로 생성할 예정.
키: 함수 넘버
값: 차분값 
  
----------------------------------------------------------------------------------------------------
## Log file format
| 함수 No | Input Argument | Input(Attribute:Dtype) |Output Argument| Output(Attribute:DType)|
|:--------|:--------:|:--------:|:--------:|:--------:|



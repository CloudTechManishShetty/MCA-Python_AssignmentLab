import datetime

ERROR_LOG_FILE = "error_log.txt"

def log_exception(error_code, exception_message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] CODE: {error_code} | EXCEPTION: {exception_message}\n"
    
    try:
        with open(ERROR_LOG_FILE, 'a') as f:
            f.write(log_entry)
        print(f"Error logged successfully with code {error_code}.")
    except Exception as e:
        print(f"CRITICAL ERROR: Could not write to log file: {e}")

def process_user_data(data):
    print(f"\n--- Processing data: {data} ---")
    
    try:
        user_id = data['user_id']
        username = data['username']
        result = 100 / data['settings']['divisor']
        print(f"Data processed for User {user_id} ({username}). Result: {result}")
        
    except KeyError as e:
        error_msg = f"Missing dictionary key: {e}"
        log_exception(error_code="4001_MISSING_KEY", exception_message=error_msg)
        print("Processing failed. Check error log.")
        
    except ZeroDivisionError as e:
        error_msg = str(e)
        log_exception(error_code="5002_ZERO_DIV", exception_message=error_msg)
        print("Processing failed. Check error log.")
        
    except Exception as e:
        error_msg = str(e)
        log_exception(error_code="9999_UNEXPECTED", exception_message=error_msg)
        print("Processing failed. Check error log.")

# Test Case 1: Missing 'username' key (KeyError)
process_user_data({'user_id': 123, 'settings': {'divisor': 1}})

# Test Case 2: Division by zero (ZeroDivisionError)
process_user_data({'user_id': 456, 'username': 'testuser', 'settings': {'divisor': 0}})

# Test Case 3: Successful execution
process_user_data({'user_id': 789, 'username': 'success', 'settings': {'divisor': 5}})

print(f"\n--- Developer Note: Check '{ERROR_LOG_FILE}' for log details. ---")
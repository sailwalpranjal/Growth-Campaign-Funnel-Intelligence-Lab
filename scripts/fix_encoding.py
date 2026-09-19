import os
import io

def fix_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            
        text = data.decode('cp1252', errors='replace')
        text = text.replace('\ufffd', '-')
        # Also remove the broken replace('', '-') if it messed it up
        
        # If I messed up by inserting '-' everywhere, I should just re-run task 3 and 1 properly.
    except Exception as e:
        print(e)

if __name__ == "__main__":
    pass

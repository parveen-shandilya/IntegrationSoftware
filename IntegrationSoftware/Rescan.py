
import os


def ReScanQR_Codes(data):
    
    
    
        
    output_folder = 'ScannedData'
    
    text_file_path = os.path.join(output_folder, 'qr_data.txt')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    if not os.path.exists(text_file_path):
        open(text_file_path, 'a').close() 
    
    # Open the text file in append mode and write only 'data' values
    with open(text_file_path, 'a') as text_file:  # 'a' mode is for appending
        for item in data:
            text_file.write(f"{item}\n")   



import os

def count_rows_in_file(file_path):
    """
    Count the number of rows (lines) in the given file.

    Args:
    file_path (str): The path to the file.

    Returns:
    int: The number of lines in the file.
    """
    if not os.path.exists(file_path):
        return 0  # If file doesn't exist, return 0

    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    
    return line_count
    


# l = [100012,100013,100014]
# ReScanQR_Codes(l)   

# l2 = [100015]
# ReScanQR_Codes(l2)   
count = 0
while(count <24):
    l = [100012,100013,100014]
    ReScanQR_Codes(l) 
    count = count_rows_in_file(r'C:/Users/lenovo/Desktop/integrationpy/IntegrationSoftware/ScannedData/qr_data.txt')
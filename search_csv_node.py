import csv
import os

class search_csv:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Path": ("STRING", {"default":""}),	
            	"Keyword": ("STRING", {"default":""}),		
                "Column": ("INT"),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Output",)

    FUNCTION = "search_csv"

    #OUTPUT_NODE = False

    CATEGORY = "utils/search_csv"

    def search_csv(self,Path,Column,Keyword):
        if not os.path.exists(Path):
            print(f"Error: The file {Path} does not exist.")
            return None

        # Open the CSV file using ";" as the delimiter
        with open(Path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')  # Use ";" as the delimiter

            # Loop through all rows to search for the Keyword in the first column
            for row in reader:
                if len(row) > 0 and row[0] == Keyword:  # Check if the first column matches the Keyword
                    if len(row) > Column:  # Ensure that the Column exists in this row
                        output_string = row[Column]
                        return (str(output_string),)
                    else:
                        print(f"Error: Row does not have a column number {Column}.")
                    return None
        # If no matching Keyword is found in the first column
            print(f"Error: The Keyword '{Keyword}' was not found in the first column.")
        return (str(output_string),)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Search CSV": search_csv
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "search_csv": "search_csv"
}
#imports
import os

def rename_files(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Loop through the files and rename them
        for filename in files:
            if filename.endswith('.png'):
                # Split the filename by the '-' character
                parts = filename.split('-')
                
                # Check if there's a '-' character in the filename
                if len(parts) > 1:
                    # Get the last part of the split (yy.png) and construct the new name
                    new_name = parts[-1]
                    
                    # Construct the full paths for the old and new filenames
                    old_path = os.path.join(folder_path, filename)
                    new_path = os.path.join(folder_path, new_name)
                    
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f'Renamed: {old_path} -> {new_path}')

        print("Renaming complete.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
folder_path = r'C:\Users\HarshPujari\Downloads\bic-compressed'
rename_files(folder_path)

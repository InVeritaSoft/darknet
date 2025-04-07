import os

def rename_images_with_extensions(folder_path, start_number, prefix="LV_Boom.", extensions=None):
    """
    Renames files in the specified folder with a given prefix and starting number for multiple extensions.

    Args:
        folder_path (str): Path to the folder containing files.
        start_number (int): The starting number for renaming.
        prefix (str): Prefix for the new filenames (default: "LV_Boom.").
        extensions (list): List of file extensions to rename (e.g., [".jpeg", ".txt"]).
    """
    if extensions is None:
        extensions = [".jpeg", ".txt"]  # Default extensions

    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Group files by their extensions
    files_by_extension = {ext: [] for ext in extensions}
    for file in os.listdir(folder_path):
        for ext in extensions:
            if file.endswith(ext):
                files_by_extension[ext].append(file)

    # Ensure all extensions have the same number of files
    file_counts = [len(files) for files in files_by_extension.values()]
    if len(set(file_counts)) > 1:
        print("Error: Mismatched file counts for the specified extensions.")
        return

    # Sort files for consistent renaming
    for ext in extensions:
        files_by_extension[ext].sort()

    # Rename files one by one
    current_number = start_number
    for i in range(file_counts[0]):  # Iterate based on the number of files
        for ext in extensions:
            old_file = files_by_extension[ext][i]
            old_path = os.path.join(folder_path, old_file)
            new_name = f"{prefix}{current_number:04d}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_file} -> {new_name}")
        current_number += 1

    print("Renaming completed.")

# Example usage
if __name__ == "__main__":
    folder = os.path.join(os.path.dirname(__file__), "images/Set14")
    start_num = 713
    prefix = "LV_Boom."
    extensions = ('.jpeg,.txt').split(",")

    rename_images_with_extensions(folder, start_num, prefix, extensions)
import os

def rename_images(folder_path, start_number, prefix="LV_Boom.", extension=".jpg"):
    """
    Renames images in the specified folder with a given prefix and starting number.

    Args:
        folder_path (str): Path to the folder containing images.
        start_number (int): The starting number for renaming.
        prefix (str): Prefix for the new filenames (default: "img_").
        extension (str): File extension for the images (default: ".jpg").
    """
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Get a sorted list of files in the folder
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(extension)])
    if not files:
        print(f"No files with extension '{extension}' found in '{folder_path}'.")
        return

    # Rename files one by one
    current_number = start_number
    for file in files:
        old_path = os.path.join(folder_path, file)
        new_name = f"{prefix}{current_number:04d}{extension}"
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")
        current_number += 1

    print("Renaming completed.")

# Example usage
if __name__ == "__main__":
    folder = os.path.join(os.path.dirname(__file__), "videos/Set2")
    start_num = 316
    prefix = "LV_Boom."
    extension = ".jpeg"

    rename_images(folder, start_num, prefix, extension)
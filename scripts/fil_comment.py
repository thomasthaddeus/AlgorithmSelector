import os

# Base directory
base_directory = "../src"  # Update this path

def add_comment_to_init_files(directory):
    # Walk through the directory structure
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "__init__.py":
                # Get the folder name
                folder_name = os.path.basename(root)

                # Create the comment
                comment = f"# {folder_name}/__init__.py\n\n"

                # Full path to the __init__.py file
                init_file_path = os.path.join(root, file)

                # Read the existing content
                with open(init_file_path, 'r') as f:
                    content = f.read()

                # Write the comment followed by the existing content
                with open(init_file_path, 'w') as f:
                    f.write(comment + content)

if __name__ == "__main__":
    add_comment_to_init_files(base_directory)

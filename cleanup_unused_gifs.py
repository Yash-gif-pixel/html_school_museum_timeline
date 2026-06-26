import os
import subprocess
import glob

def main():
    images_dir = "images"
    pattern = os.path.join(images_dir, "event_*.gif")
    files_to_remove = glob.glob(pattern)
    
    print(f"Found {len(files_to_remove)} event-specific GIF files to remove.")
    
    removed_count = 0
    for file_path in files_to_remove:
        # Check if the file is tracked in git
        try:
            # We use git rm to remove it from both index and working tree
            subprocess.run(["git", "rm", "-f", file_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            removed_count += 1
        except subprocess.CalledProcessError:
            # If not tracked, just delete the file from disk
            if os.path.exists(file_path):
                os.remove(file_path)
                removed_count += 1
                
    print(f"Successfully removed {removed_count} GIF files.")

if __name__ == "__main__":
    main()

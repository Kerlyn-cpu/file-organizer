from pathlib import Path

Organize = Path.home()/"python"

categories = {
    "images" :[".jpeg"],
    "pdf files" :[".pdf",".docx"],
    "text files" :[".txt"],
    "apk files" :[".apk"],
    "others" : []
}
items = Organize.iterdir()
for item in items:
    if item.is_file():
        ext = item.suffix.lower()
        found_match = False
        for folder_name,extension in categories.items():
            if ext in extension:
                old_path = item 
                new_folder = Organize/folder_name
                new_folder.mkdir(parents=True,exist_ok=True)
                new_path = new_folder/ item.name
                old_path.replace(new_path)
                print("✅ files moved succesfully")
                found_match = True
                break 
        if not found_match:
            others_folder = Organize/"others" 
            others_folder.mkdir(parents=True,exist_ok=True)
            item.replace(others_folder/item.name)      
            print(f"✅Moved{item.name} to others")
                   


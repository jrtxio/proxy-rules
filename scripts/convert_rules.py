import os
import glob

def convert_surge_to_clash():
    # Define paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    surge_dir = os.path.join(root_dir, 'surge')
    clash_dir = os.path.join(root_dir, 'clash')

    # Ensure output directory exists
    if not os.path.exists(clash_dir):
        os.makedirs(clash_dir)
        print(f"Created directory: {clash_dir}")

    # Find all .list files
    list_files = glob.glob(os.path.join(surge_dir, '*.list'))
    
    if not list_files:
        print(f"No .list files found in {surge_dir}")
        return

    print(f"Found {len(list_files)} files to convert...")

    for file_path in list_files:
        filename = os.path.basename(file_path)
        name_without_ext = os.path.splitext(filename)[0]
        output_path = os.path.join(clash_dir, f"{name_without_ext}.yml")
        
        print(f"Converting {filename} -> {os.path.basename(output_path)}")
        
        headers = []
        rules = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            # Simple parser
            for line in lines:
                stripped = line.strip()
                if not stripped:
                    continue
                
                if stripped.startswith('#') or stripped.startswith(';'):
                    # Keep headers/comments that appear at the top or generally preserve comments?
                    # For YAML payload format, comments inside the list are tricky.
                    # Best to keep top-level comments as header, ignore inline comments for simplicity
                    # unless we want to be very sophisticated.
                    # Let's just preserve the top header block.
                    if not rules: 
                        headers.append(stripped)
                else:
                    # It's a rule
                    # Some Surge rules might have comments at the end of the line, e.g. "DOMAIN,x,DIRECT # comment"
                    # But usually .list files are clean.
                    # We'll just take the line content.
                    rules.append(stripped)

        # Write YAML
        with open(output_path, 'w', encoding='utf-8') as f:
            # Write headers
            if headers:
                for h in headers:
                    f.write(f"{h}\n")
            
            f.write("payload:\n")
            for rule in rules:
                # Quote the rule to be safe, though not strictly required for simple domains
                # But simple domains don't need quotes. Complex chars might.
                # Let's check if it contains special chars.
                # Single quotes are safe for most things except single quotes.
                f.write(f"  - '{rule}'\n")

    print("Conversion complete.")

if __name__ == "__main__":
    convert_surge_to_clash()

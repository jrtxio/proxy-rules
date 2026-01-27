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
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            # Separate header comments from body
            header_comments = []
            body_lines = []
            is_header = True
            
            for line in lines:
                stripped = line.strip()
                if is_header:
                    if not stripped: 
                        header_comments.append(line)
                    elif stripped.startswith('#') or stripped.startswith(';'):
                        header_comments.append(line)
                    else:
                        is_header = False
                        body_lines.append(line)
                else:
                    body_lines.append(line)
            
            # Write Header
            for line in header_comments:
                f.write(line)
            
            f.write("payload:\n")
            
            # Write Body
            for line in body_lines:
                stripped = line.strip()
                if not stripped:
                    f.write(line) # Preserve empty lines
                    continue
                
                if stripped.startswith('#') or stripped.startswith(';'):
                    # Indent comments inside payload
                    f.write(f"  {stripped}\n")
                else:
                    # Filter unsupported rules for Clash Rule Providers
                    # Clash Rule Providers typically support: DOMAIN, DOMAIN-SUFFIX, DOMAIN-KEYWORD, IP-CIDR, IP-CIDR6, CLASSICAL
                    # PROCESS-NAME and USER-AGENT are usually strictly local rules
                    if stripped.startswith('PROCESS-NAME') or stripped.startswith('USER-AGENT'):
                        print(f"  [WARN] Skipping unsupported rule for Clash provider: {stripped}")
                        f.write(f"  # [SKIPPED] {stripped}\n")
                        continue

                    # It's a rule
                    f.write(f"  - '{stripped}'\n")

    print("Conversion complete.")

if __name__ == "__main__":
    convert_surge_to_clash()

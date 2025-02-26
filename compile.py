import os
import subprocess
import sys
import logging
from pathlib import Path
import shutil

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    filename='compilation_log.txt')

def find_autoit_dll():
    """Find the AutoItX3_x64.dll"""
    possible_locations = [
        r'C:\Program Files (x86)\AutoIt3\AutoItX',
        r'C:\Program Files\AutoIt3\AutoItX',
        os.path.join(sys.prefix, 'Lib', 'site-packages', 'autoit', 'lib')
    ]
    
    for location in possible_locations:
        dll_path = os.path.join(location, 'AutoItX3_x64.dll')
        if os.path.exists(dll_path):
            return dll_path
    
    logging.error("AutoItX3_x64.dll not found")
    return None

def compile_script(script_path, additional_data=None, exclude_patterns=None):
    """Compile a single Python script to executable."""
    try:
        # Skip compilation for certain files or patterns
        if exclude_patterns and any(pattern in script_path for pattern in exclude_patterns):
            logging.info(f"Skipping {script_path}")
            return False

        logging.info(f"Compiling {script_path}")
        
        # Prepare PyInstaller command
        cmd = [
            'pyinstaller', 
            '--onefile', 
            '--windowed',
            '--name', os.path.splitext(os.path.basename(script_path))[0]
        ]
        
        # Add additional data files if provided
        if additional_data:
            for data in additional_data:
                cmd.extend(['--add-data', data])
        
        
        # Add hidden imports for common libraries
        hidden_imports = [
            '--hidden-import', 'pyautogui',
            '--hidden-import', 'autoit',
            '--hidden-import', 'pynput',
            '--hidden-import', 'keyboard'
        ]
        cmd.extend(hidden_imports)
        
        cmd.append(script_path)
        
        # Run PyInstaller
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            logging.info(f"Successfully compiled {script_path}")
            return True
        else:
            logging.error(f"Compilation failed for {script_path}")
            logging.error(result.stderr)
            return False
    except Exception as e:
        logging.error(f"Error compiling {script_path}: {e}")
        return False

def find_python_scripts(base_path):
    """Find all Python scripts in the workspace, excluding certain directories."""
    python_scripts = []
    exclude_dirs = {'venv', '.git', 'dist', '__pycache__'}
    
    for root, dirs, files in os.walk(base_path):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Find .py files
        for file in files:
            if file.endswith('.py') and file != 'compile.py':
                full_path = os.path.join(root, file)
                python_scripts.append(full_path)
    
    return python_scripts

def main():
    # Base workspace path
    workspace_path = 'e:/automateESX'
    
    # Find AutoItX DLL
    autoit_dll = find_autoit_dll()
    
    if not autoit_dll:
        logging.error("Could not find AutoItX3_x64.dll")
        return
    
    # Create distribution folder
    dist_folder = Path(os.path.join(workspace_path, 'dist'))
    dist_folder.mkdir(exist_ok=True)
    
    # Prepare additional data
    additional_data = [
        f'{autoit_dll}{os.pathsep}autoit/lib'  # This tells PyInstaller to include the DLL
    ]
   
    # Exclude patterns
    exclude_patterns = [
        'test_', 
        'setup.py', 
        'compile.py',
        '__init__.py'
    ]
    
    # Find all Python scripts
    scripts_to_compile = find_python_scripts(workspace_path)
    
    # Compile each script
    successful_compilations = []
    failed_compilations = []
    
    for script in scripts_to_compile:
        try:
            if compile_script(script, additional_data, exclude_patterns):
                successful_compilations.append(script)
            else:
                failed_compilations.append(script)
        except Exception as e:
            logging.error(f"Unexpected error compiling {script}: {e}")
            failed_compilations.append(script)
    
    # Log compilation summary
    logging.info("Compilation Summary:")
    logging.info(f"Successfully compiled {len(successful_compilations)} scripts")
    logging.info(f"Failed to compile {len(failed_compilations)} scripts")
    
    if failed_compilations:
        logging.error("Failed Scripts:")
        for script in failed_compilations:
            logging.error(script)
    
    logging.info("Compilation process completed.")

if __name__ == '__main__':
    main()
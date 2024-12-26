import os
import subprocess

def create_project_structure():
    directories = ['src', 'tests', 'docs', 'data']  # Added data directory
    [os.makedirs(dir, exist_ok=True) for dir in directories]
    
def setup_venv():
    subprocess.run(['python', '-m', 'venv', 'venv'], check=True)
    print("Virtual environment created - please activate it manually with:")
    print("venv\\Scripts\\activate (Windows)")

def install_poetry():
    subprocess.run(['pip', 'install', 'poetry'], check=True)
    subprocess.run(['poetry', 'init', '--no-interaction'], check=True)

def init_git():
    subprocess.run(['git', 'init'], check=True)
    with open('.gitignore', 'w') as f:
        f.write('venv/\n')
        f.write('__pycache__/\n')
        f.write('.pytest_cache/\n')
        f.write('/data/*\n')  # Added to ignore data files

def main():
    try:
        print("Creating project structure...")
        create_project_structure()
        
        print("\nSetting up virtual environment...")
        setup_venv()
        
        print("\nNOTE: Please activate your virtual environment before continuing!")
        response = input("Have you activated the virtual environment? (y/n): ")
        if response.lower() != 'y':
            print("Please activate the virtual environment and run this script again.")
            return
            
        print("\nInstalling Poetry...")
        install_poetry()
        
        print("\nInstalling and initializing DVC...")
        install_dvc()
        
        print("\nInitializing git repository...")
        init_git()
        
        print("\nSetup complete!")
        print("\nRemember to:")
        print("1. Configure your DVC remote storage")
        print("2. Add your data files to DVC tracking with 'dvc add data/your_file'")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during setup: {e}")
        return

if __name__ == "__main__":
    main()
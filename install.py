import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

# List of packages to install
packages = [
    "boto3==1.24.84",
    "botocore-stubs==1.27.86",
    "dill==0.3.5.1",
    "dnspython==2.2.1",
    "fastapi==0.78.0", 
    "from-root==1.0.2",
    "imbalanced-learn",
    "mypy-boto3-s3==1.24.76",
    "pip-chill==1.0.1",
    "pymongo==4.2.0",
    "python-dotenv==0.21.0",
    "types-s3transfer==0.6.0.post4",
    "uvicorn==0.18.3",
    "watchfiles==0.17.0",
    "websockets==10.3",
    "wincertstore==0.2",
    "xgboost==1.6.2",
    "python-multipart",
    "neuro_mf",
    "evidently==0.4.33"  # Make sure evidently is last
]

print("Installing all dependencies...")
for package in packages:
    install_package(package)

print("\n🎉 Installation completed! Now run: python app.py")
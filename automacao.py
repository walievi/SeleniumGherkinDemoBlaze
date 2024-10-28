import subprocess

def run_tests():
    subprocess.run(['behave'])

if __name__ == "__main__":
    run_tests()
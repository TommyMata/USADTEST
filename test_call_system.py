"""
Script to test the complete call simulation system.
Starts the middleware server and runs the simulator automatically.
"""
import subprocess
import time
import sys
import os

def main():
    print("="*70)
    print("PHONE CALL TRANSCRIPTION SYSTEM")
    print("="*70)
    print()
    
    # Start the middleware server
    print("[1] Starting middleware server...")
    server_process = subprocess.Popen(
        [sys.executable, "middleware.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=os.getcwd()
    )
    
    # Wait for server to start
    print("    Waiting for server to be ready...\n")
    time.sleep(3)
    
    # Run the call simulator
    print("[2] Running call simulator...")
    print()
    
    try:
        result = subprocess.run(
            [sys.executable, "call_simulator.py"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
    except subprocess.TimeoutExpired:
        print("[WARNING] Simulator took too long")
    except Exception as e:
        print(f"[ERROR] Error running simulator: {e}")
    
    # Wait a bit for server to process
    print("\n[3] Waiting for server processing...")
    time.sleep(2)
    
    # Stop the server
    print("\n[4] Stopping middleware server...\n")
    server_process.terminate()
    
    # Capture server output
    try:
        stdout, stderr = server_process.communicate(timeout=5)
        print("="*70)
        print("MIDDLEWARE SERVER OUTPUT:")
        print("="*70)
        print(stdout)
        if stderr:
            print("\nERRORS:", stderr)
    except subprocess.TimeoutExpired:
        server_process.kill()
        print("[WARNING] Server did not stop correctly")
    
    print("\n" + "="*70)
    print("[SUCCESS] Test completed")
    print("="*70)

if __name__ == "__main__":
    main()

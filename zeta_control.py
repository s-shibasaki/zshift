import zplatform
import subprocess
import json

def zeta_shift(signal, shift_factor):
    if zplatform.is_qenv():
        command = [
            "qsignal-processor",
            "--mode", "zeta-shift",
            "--input", json.dumps(signal),
            "--shift-factor", str(shift_factor),
            "--quantum-precision", "high"
        ]
        
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
            
            shifted_signal = json.loads(result.stdout)
            
            print("Zeta Shift completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error in signal processing: {e}")
            print(f"Error output: {e.stderr}")
            shifted_signal = signal
        except json.JSONDecodeError:
            print("Error decoding the output from processor.")
            shifted_signal = signal
    else:
        shifted_signal = [s + shift_factor for s in signal]
    
    return shifted_signal


```
import zeta_control

signal = load_signal("input.dat")

shift_factor = 0.5

shifted_signal = zeta_control.zeta_shift(signal, shift_factor)

save_signal(shifted_signal, "output.dat")
```
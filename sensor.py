import os 
import time 
# Ruta base del sensor 1-Wire 
BASE_DIR = "/sys/bus/w1/devices/" 
SENSOR_PREFIX = "28-" 
SENSOR_FILE = "w1_slave" 
def find_sensor(): 
for d in os.listdir(BASE_DIR): 
if d.startswith(SENSOR_PREFIX): 
return os.path.join(BASE_DIR, d, SENSOR_FILE) raise FileNotFoundError("No s'ha trobat cap sensor DS18B20") 
def read_temp(sensor_path): 
with open(sensor_path, "r") as f: 
lines = f.readlines() 
while "YES" not in lines[0]: 
time.sleep(0.2) 
with open(sensor_path, "r") as f: 
lines = f.readlines() 
temp_str = lines[1].split("t=")[1] 
temp_c = float(temp_str) / 1000.0 
return temp_c 
def main(): 
sensor_path = find_sensor() 
print("Sensor trobat:", sensor_path) 
while True: 
temp = read_temp(sensor_path)
print(f"Temperatura: {temp:.3f} °C") time.sleep(1) 
if __name__ == "__main__": 
main()

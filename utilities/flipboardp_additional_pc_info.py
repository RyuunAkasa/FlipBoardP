import platform
import psutil


# 1. OS Information

def get_pc_info():
        
    try:

        os = platform.system()
        release = platform.release()
        version = platform.version()



        # 2. Charge/Battery Information
        battery = psutil.sensors_battery()
        charge = ""

        if battery:
            charge = f"Battery Charge: {battery.percent}%"
            plugged = "Power Plugged" if battery.power_plugged else "Not Plugged In"
        else:
            charge = "Battery info not available."

        info = f"{os} {release} {version} \n{charge} {plugged}"


        return info
    except :

        return None
    


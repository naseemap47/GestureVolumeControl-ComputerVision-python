import subprocess


def get_master_volume():
    proc = subprocess.Popen('/usr/bin/amixer sget Master', shell=True, stdout=subprocess.PIPE)
    amixer_stdout = str(proc.communicate()[0], 'UTF-8').split('\n')[4]
    proc.wait()
    find_start = amixer_stdout.find('[') + 1
    find_end = amixer_stdout.find('%]', find_start)
    return float(amixer_stdout[find_start:find_end])


def set_master_volume(volume):
    val = volume
    val = float(int(val))
    proc = subprocess.Popen('/usr/bin/amixer sset Master ' + str(val) + '%', shell=True, stdout=subprocess.PIPE)
    proc.wait()


print("Current volume: ", get_master_volume())
set_master_volume(0)
print("Current volume (changed): ", get_master_volume())
set_master_volume(50)
print("Current volume (changed): ", get_master_volume())

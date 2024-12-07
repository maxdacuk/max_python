import re

string = '2024-11-19 06:53:59.436;activate;88.102.184.131;1068573;Mode:0;MachineId:zXh2eerGUkNKZHpHaccb3w==;"MachineName:DESKTOP-2TNSA0V";"ModelName:XPS 13 9360";UserId:AAAAAAAAAAAAAAAAAAAAAA==;"UserName:";"EditorVersion:9.3.361.0";ResultStatus:success;Replacement:-;"Message:";"Way:Online"'

machine_id_match = re.search(r'MachineId:([\w=]+)', string)
editor_version_match = re.search(r'EditorVersion:([\d.]+)', string)
number_match = re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', string)

machine_id = machine_id_match.group(1) if machine_id_match else None
editor_version = editor_version_match.group(1) if editor_version_match else None
number = number_match.group(0) if number_match else None


print(f"MachineId: {machine_id}")
print(f"EditorVersion: {editor_version}")
print(f"Numbers: {number}")
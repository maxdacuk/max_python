import xml.etree.ElementTree as ET

# Створення кореневого елемента
root = ET.Element("students")

# Список студентів
students = [
    {"first_name": "Maxym", "last_name": "Diachuk", "age": "15"},
    {"first_name": "Pavlo", "last_name": "Stadnyk", "age": "15"},
    {"first_name": "Arsen", "last_name": "Olih", "age": "16"}
]

# Додавання студентів до XML
for student in students:
    student_elem = ET.SubElement(root, "student")
    
    first_name_elem = ET.SubElement(student_elem, "first_name")
    first_name_elem.text = student["first_name"]
    
    last_name_elem = ET.SubElement(student_elem, "last_name")
    last_name_elem.text = student["last_name"]
    
    age_elem = ET.SubElement(student_elem, "age")
    age_elem.text = student["age"]

# Створення дерева та збереження в XML файл
tree = ET.ElementTree(root)
tree.write("students.xml", encoding="utf-8", xml_declaration=True)

print("XML-файл створено!")

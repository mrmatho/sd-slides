import xml.etree.ElementTree as ET

class_tree = ET.parse('class.xml')

root = class_tree.getroot()

for student in root.findall('student'):
    name = student.find('name').text
    print(f"Name: {name}")
    assessments = student.findall('assessment')
    for assess in assessments:
        title = assess.find('title').text
        grade = assess.find('grade').text
        print(f" - *{title}*: {grade}")
    new_assess = input(f"Would you like to add an assessment for {name}?:")
    if new_assess == 'Y':
        new_title = input("Enter assessment title:")
        new_grade = input("Enter assessment grade:")
        new_assess_tag = ET.SubElement(student, "assessment")
        new_title_tag = ET.SubElement(new_assess_tag, "title")
        new_grade_tage = ET.SubElement(new_assess_tag, "grade")
        new_title_tag.text = new_title
        new_grade_tage.text = new_grade
        class_tree.write('class.xml', encoding='unicode', xml_declaration=True)
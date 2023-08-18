import xmlschema as xml


XML_SCHEMA = xml.XMLSchema("EmployeeXml\employee_schema.xsd")

if XML_SCHEMA.is_valid("EmployeeXml\employee.xml"):
    print("The xml is vaild")
else:
    print("Sorry, xml is not well formed or valid")
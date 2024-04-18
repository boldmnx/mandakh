import xml.dom.minidom as dom

# Function to parse XML file


def parse_xml(file_path):
    # Parse XML file
    dom_tree = dom.parse(file_path)
    # Get the root element
    root = dom_tree.documentElement

    # Example: Accessing elements and attributes
    items = root.getElementsByTagName("item")
    for item in items:
        name = item.getAttribute("name")
        price = item.getAttribute("price")
        print("Item:", name, "Price:", price)


# Function to create XML file
def create_xml(file_path):

    # Create XML document
    doc = dom.Document()

    # Create root element
    root = doc.createElement("items")
    doc.appendChild(root)

    # Add items
    items = [
        {"name": "Apple", "price": "1.50"},
        {"name": "Banana", "price": "0.75"},
        {"name": "Orange", "price": "1.00"}
    ]

    for item_data in items:
        item = doc.createElement("item")
        item.setAttribute("name", item_data["name"])
        item.setAttribute("price", item_data["price"])
        root.appendChild(item)

    # Write to file
    with open(file_path, "w") as file:
        doc.writexml(file, indent="\t", addindent="\t", newl="\n")


# Path to XML file
file_path = "items.xml"

# Create XML file
create_xml(file_path)

# Read and parse XML file
parse_xml(file_path)

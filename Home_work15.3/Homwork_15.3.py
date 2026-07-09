
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("xml_searcher")


xml_path = BASE_DIR  /"result3_Zabolotnyi.xml"



def find_incoming_by_group_number(file_path, group_number):
    if not file_path.exists():
        logger.error(f"XML-файл не знайдено за шляхом: {file_path}")
        return None

    try:

        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall('.//group'):
            number_node = group.find('number')

            if number_node is not None and number_node.text == str(group_number):
                incoming_node = group.find('.//timingExbytes/incoming')

                if incoming_node is not None:
                    return incoming_node.text
                else:
                    logger.warning(f"Для групи №{group_number} не знайдено тег timingExbytes/incoming")
                    return None

        logger.warning(f"Групу з номером {group_number} не знайдено в файлі.")
        return None

    except ET.ParseError as e:
        logger.error(f"Помилка читання XML структури: {e}")
        return None

print("\n--- Старт пошуку в XML ---")

search_number = "10"
result = find_incoming_by_group_number(xml_path, search_number)

if result is not None:
    logger.info(f"Для group/number = {search_number} значення timingExbytes/incoming становить: {result}")
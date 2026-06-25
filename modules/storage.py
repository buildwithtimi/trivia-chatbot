import json
from pathlib import Path


# Path to the knowledge base
KNOWLEDGE_FILE = Path("data/knowledge.json")


def load_knowledge():
    """
    Load all knowledge from the JSON file.

    Returns:
        list: List of question-answer objects.
    """

    try:
        with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Knowledge file not found.")
        return []

    except json.JSONDecodeError:
        print("Knowledge file contains invalid JSON.")
        return []


def save_knowledge(data):
    """
    Save all knowledge to the JSON file.

    Args:
        data (list): List of question-answer objects.
    """

    with open(KNOWLEDGE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
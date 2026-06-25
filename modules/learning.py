from modules.storage import load_knowledge


def find_answer(question):
    """
    Search the knowledge base for a question.

    Args:
        question (str): The user's question.

    Returns:
        str | None: The answer if found, otherwise None.
    """

    knowledge = load_knowledge()

    normalized_question = question.strip().lower()

    for item in knowledge:
        stored_question = item["question"].strip().lower()

        if stored_question == normalized_question:
            return item["answer"]

    return None
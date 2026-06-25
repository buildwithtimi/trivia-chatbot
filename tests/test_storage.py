from modules.storage import load_knowledge

knowledge = load_knowledge()

print(f"Questions loaded: {len(knowledge)}")
print()
print("First question:")
print(knowledge[0])
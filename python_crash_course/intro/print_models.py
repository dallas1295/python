# # Start with a list
# unstarted_ideas = [
#     "journaly",
#     "todo thingy",
#     "ai cli app",
# ]
#
# completed_ideas = []
# while unstarted_ideas:
#     current_idea = unstarted_ideas.pop()
#     print(f"Starting idea: {current_idea}")
#     completed_ideas.append(current_idea)
#
# print("\nThe following ideas have been completed")
# for completed_idea in completed_ideas:
#     print(completed_idea)


def start_ideas(unstarted_ideas, completed_ideas):
    """Simulate starting the ideas in the list"""
    while unstarted_ideas:
        current_idea = unstarted_ideas.pop()
        print(f"Starting idea: {current_idea}")
        completed_ideas.append(current_idea)


def show_completed(completed_ideas):
    """Show all completed ideas"""

    print("\nThe following ideas have been completed:")
    for completed_idea in completed_ideas:
        print(completed_idea)


unstarted_ideas = [
    "journaly",
    "todo thingy",
    "ai cli app",
]
completed_ideas = []

# start_ideas(unstarted_ideas, completed_ideas)
# This [:] uses a copy of the list so when they are moved to completed they do not empty the list
start_ideas(unstarted_ideas[:], completed_ideas)

show_completed(completed_ideas)

from q_learning_table import QLearningTable


class QAgent:
    name = "Q Agent"

    def __init__(self):
        self.Q = None

    def choose_action(self, observations):
        if self.Q is None:
            self.Q = QLearningTable(
                actions = list(product())
            )


    # def step(self, observations):
    #     if self.Q is None:
    #         self.Q = QLearningTable(
    #             actions = list(product())
    #         )

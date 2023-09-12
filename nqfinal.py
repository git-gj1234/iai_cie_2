import random

N = 8

def random_state():
    return [random.randint(0, N-1) for _ in range(N)]

def calculate_attack_count(state):
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def hill_climbing():
    current_state = random_state()
    current_attacks = calculate_attack_count(current_state)

    while current_attacks > 0:
        neighbor_state = list(current_state)
        row_to_change = random.randint(0, N-1)
        new_col = random.randint(0, N-1)
        neighbor_state[row_to_change] = new_col

        neighbor_attacks = calculate_attack_count(neighbor_state)

        if neighbor_attacks <= current_attacks:
            current_state = neighbor_state
            current_attacks = neighbor_attacks

    return current_state

def print_board(state):
    for row in state:
        print(" ".join("Q" if col == row else "." for col in range(N)))

if __name__ == "__main__":
    final_state = hill_climbing()
    print_board(final_state)
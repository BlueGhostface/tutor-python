from collections import Counter

def score_dice(dice):
    counts = Counter(dice)
    score = 0

    for face, count in counts.items():
        # Handle triples
        if count >= 3:
            match face:
                case 1:
                    score += 1000
                case 2:
                    score += 200
                case 3:
                    score += 300
                case 4:
                    score += 400
                case 5:
                    score += 500
                case 6:
                    score += 600
            count -= 3

        # Handle leftover 1s and 5s
        if face == 1:
            score += count * 100
        elif face == 5:
            score += count * 50

    return score

# Example usage
dice_roll = [1, 1, 1, 5, 5, 2]
dice_roll2 = [1, 1, 5, 5, 5, 3]
dice_roll3 = [1, 2, 1, 5, 5, 2]
print(score_dice(dice_roll))  # Output: 1100
print(score_dice(dice_roll2))  # Output: 700
print(score_dice(dice_roll3))  # Output: 300
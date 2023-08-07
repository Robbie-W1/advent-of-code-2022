def process_elves_from_file(filename: str) -> list[list[int]]:
    with open('input.txt', 'r') as f:
        elves = f.read().split('\n\n')
        elves = [elf.split('\n') for elf in elves]
        return [
            [int(calorie) for calorie in elf] for elf in elves
        ]
        
        
def get_max_calories(elves: list[list[int]], num_elves: int = 0) -> int | list[int]:
    """Return the elf with the most calories."""
    if num_elves == 0:
        return max(sum(calories) for calories in elves)
    
    for i in range(num_elves):
        summed_calories = [sum(calories) for calories in elves]
        return sum(sorted(summed_calories, reverse=True)[:num_elves])
        

def main() -> None:
    elves = process_elves_from_file('input.txt')
    print(f'Part one: {get_max_calories(elves)} calories')
    print(f'Part two: {get_max_calories(elves, num_elves=3)} calories')

if __name__ == '__main__':
    main()
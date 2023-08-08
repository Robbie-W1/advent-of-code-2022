def get_priorty_from_letter(bag_contents: str):
    for item in bag_contents:
        if item.islower():
            return (ord(item) - 96)
        else:
            return (ord(item) - 38)

def part_1():
    with open('input.txt', 'r') as f:
        
        count = 0
        file_contents = f.readlines()
        for line in file_contents:
            line = line.strip()
            mid_point = len(line)//2
            bag_1 = line[mid_point:]
            bag_2 = line[:mid_point]
            
            common_items = set(bag_1) & set(bag_2)
            common_items_priority = get_priorty_from_letter(common_items)
            count += common_items_priority
            
    return count            

def part_2():
    with open('input.txt', 'r') as f:
        file_contents = f.readlines()
        sacks = [line.strip() for line in file_contents]
        
        priorities_sum = 0
        for i in range(0, len(sacks), 3):
            common = set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2])
            priorities_sum += get_priorty_from_letter(common)
            
        return priorities_sum
            
            
def main() -> None:
    print(f'Part one: {part_1()}')
    assert part_1() == 7446
    print(f'Part two: {part_2()}')
    

if __name__ == '__main__':
    main()
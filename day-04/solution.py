import re

def are_pairs_containing(min_1: int, max_1: int, min_2: int, max_2: int) -> bool:
    return (min_1 <= min_2 and max_1 >= max_2) or (min_2 <= min_1 and max_2 >= max_1)

def are_pairs_overlapping(min_1: int, max_1: int, min_2: int, max_2: int) -> bool:
    return (min_1 <= min_2 and max_1 >= min_2) or (min_2 <= min_1 and max_2 >= min_1)
    
    
def part_1() -> int:
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        contents = []
        for line in lines:
            min_1, max_1, min_2, max_2 = map(int, re.findall(r'\d+', line))
            contents.append((min_1, max_1, min_2, max_2))
        
        containing_count = 0
        for item in contents:
            containing_count += are_pairs_containing(*item)
            
        return containing_count
        
def part_2() -> int:
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        contents = []
        for line in lines:
            min_1, max_1, min_2, max_2 = map(int, re.findall(r'\d+', line))
            contents.append((min_1, max_1, min_2, max_2))
        
        overlapping_count = 0
        for item in contents:
            overlapping_count += are_pairs_overlapping(*item)
            
        return overlapping_count
        
            
            
    
def main() -> None:
    print(f'Part one: {part_1()}')
    print(f'Part two: {part_2()}')
    
if __name__ == "__main__":
    main()
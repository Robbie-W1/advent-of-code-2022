import re

def move_box_crane_9000(stacks: list[list[str]], num_boxes: int, from_stack: int, to_stack: int) -> list[list[str]]:
    for _ in range(num_boxes):
        free_box = stacks[from_stack-1].pop(0)
        stacks[to_stack-1].insert(0, free_box)
    return stacks
    

def move_box_crane_9001(stacks: list[list[str]], num_boxes: int, from_stack: int, to_stack: int) -> list[list[str]]:
    free_boxes = []
    for _ in range(num_boxes):
        free_boxes.append(stacks[from_stack-1].pop(0))
    for free_box in free_boxes[::-1]:
        stacks[to_stack-1].insert(0, free_box)
    return stacks
    
def get_message(stacks) -> str:
    rmessage = [stack[0] for stack in stacks]
    return ''.join(rmessage)

def set_up() -> tuple[list[list[str], list[str]]]:
    with open('input.txt', 'r') as f:
        stacks_str, instructions = f.read().split('\n\n')
        stacks_list = stacks_str.splitlines()
        num_stacks = int(stacks_list[-1].split(' ')[-2]) # last number in stack numbers row
        stacks_list = stacks_list[:-1]
        
        stacks = [[] for _ in range(num_stacks)]
        for row in stacks_list:
            for index, item in enumerate(row[1::4]):
                if item != ' ':
                    stacks[index].append(item)
                    
    return stacks, instructions

def part_1():
    
    stacks, instructions = set_up()
        
    for instruction in instructions.splitlines():
        nums = re.findall(r'\d+', instruction)
        num_boxes, from_stack, to_stack = map(int, nums)
        
        stacks = move_box_crane_9000(stacks, num_boxes, from_stack, to_stack)
        
                
    return get_message(stacks)
    
def part_2():
        
        stacks, instructions = set_up()
            
        for instruction in instructions.splitlines():
            nums = re.findall(r'\d+', instruction)
            num_boxes, from_stack, to_stack = map(int, nums)
            
            stacks = move_box_crane_9001(stacks, num_boxes, from_stack, to_stack)
            
        return get_message(stacks)
    

def main():
    print(f'Part one: {part_1()}')
    print(f'Part two: {part_2()}')
    
if __name__ == "__main__":
    main()

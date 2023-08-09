
def find_marker(text: str, window_length: int) -> int:
    for i, _ in enumerate(text):
            window = text[i:i+window_length]
            if len(window) == len(set(window)):
                return i + window_length
            
def part_1():
    with open('input.txt', 'r') as f:
        chars = f.read()
        
        return find_marker(chars, 4)
        
        
def part_2():
    with open('input.txt', 'r') as f:
        chars = f.read()
        
        return find_marker(chars, 14)

def main():
    print(f'Part one: {part_1()}')
    print(f'Part two: {part_2()}')
    
if __name__ == "__main__":
    main()
